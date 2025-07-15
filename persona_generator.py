import os
import praw
from dotenv import load_dotenv
from urllib.parse import urlparse
import subprocess

# Load environment variables from .env file for Reddit API credentials
load_dotenv()

# Set up Reddit API connection using PRAW
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username_from_url(url):
    # Parse the Reddit profile URL to grab the username
    path = urlparse(url).path
    parts = path.strip("/").split("/")
    # Check if the URL follows the /user/username pattern
    return parts[1] if len(parts) > 1 and parts[0] == "user" else None

def fetch_reddit_content(username, limit=20):
    # Fetch recent comments and posts for the given Reddit user
    user = reddit.redditor(username)
    content = []
    try:
        # Grab up to 'limit' recent comments
        for comment in user.comments.new(limit=limit):
            content.append({
                "type": "comment",
                "text": comment.body,
                "url": f"https://www.reddit.com{comment.permalink}"
            })
        # Grab up to 'limit' recent posts (title + body)
        for submission in user.submissions.new(limit=limit):
            text = submission.title + "\n\n" + (submission.selftext or "")
            content.append({
                "type": "post",
                "text": text,
                "url": f"https://www.reddit.com{submission.permalink}"
            })
    except Exception as e:
        print(f"😕 Trouble fetching data for {username}: {e}")
    return content

def build_prompt(content, username):
    # Create a prompt for the phi model with up to 10 content items
    blocks = []
    for i, item in enumerate(content[:10]):
        block = f"{i+1}. Type {item['type'].capitalize()}\nText {item['text']}\nURL {item['url']}"
        blocks.append(block)
    prompt = "\n\n".join(blocks)

    # Construct the full prompt with instructions for the phi model
    return f"""
You are an AI that analyzes Reddit user activity to create a user persona.
Generate a structured persona in plain text, following this format (no bold, colons, or markdown):

🧠 USER PERSONA u/{username}

🔸 Summary
Write a single paragraph summarizing the user's behavior, tone, and interests.

🌱 Interests and Hobbies
Describe key interests in one sentence.
- Relevant quote
  Source URL

🗣️ Communication Style
Describe the user's writing or interaction style in one sentence.
- Relevant quote
  Source URL

📌 Common Themes
List common topics or patterns in their activity.
- Relevant quote
  Source URL

Use only emoji headings and plain text, no extra formatting like ** or ::.

Here’s the Reddit user data to analyze:

{prompt}
"""

def run_ollama_phi(prompt):
    # Run the phi model via Ollama to generate the persona
    try:
        result = subprocess.run(
            ['ollama', 'run', 'phi'],
            input=prompt.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.stdout.decode('utf-8', errors='ignore').strip()
    except Exception as e:
        print(f"😓 Error running the phi model: {e}")
        return None

def save_persona(username, persona_text, content):
    # Save the generated persona to a text file in the outputs folder
    os.makedirs("outputs", exist_ok=True)
    path = os.path.join("outputs", f"{username}_persona.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"🧠 USER PERSONA u/{username}\n\n")
        f.write(persona_text.strip())
        f.write("\n\n📎 Citations\n")
        # Add citations for up to 10 content items
        for i, item in enumerate(content[:10]):
            f.write(f"{i+1}. {item['url']}\n")

    print(f"🎉 Persona saved to: {path}")

def main():
    # Main function to run the persona generator
    url = input("🔗 Enter Reddit user profile URL: ").strip()
    username = extract_username_from_url(url)

    if not username:
        print("❌ That URL doesn’t look like a valid Reddit profile.")
        return

    print(f"📥 Pulling content for {username}...")
    content = fetch_reddit_content(username)

    if not content:
        print("❌ No content found for this user.")
        return

    print("🤖 Generating persona with the phi model...")
    prompt = build_prompt(content, username)
    persona = run_ollama_phi(prompt)

    if persona:
        save_persona(username, persona, content)
    else:
        print("❌ Failed to generate the persona.")

if __name__ == "__main__":
    main()