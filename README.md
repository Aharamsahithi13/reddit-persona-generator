Reddit User Persona Generator

This project dives into a Reddit user’s recent posts and comments to create a detailed, qualitative persona. It captures their personality, interests, and style, complete with real citations from their Reddit activity. Powered by the `phi` model through [Ollama](https://ollama.com/), it runs entirely locally—no external APIs needed!

🚀 What It Does

- 🧑‍💻 Builds a structured persona based on a Reddit user’s profile
- 🤖 Uses the lightweight `phi` model via Ollama for local processing
- 🔗 Includes real Reddit post/comment links for authenticity
- 📝 Outputs a clean, easy-to-read text file with emoji-organized sections
- 🔒 Runs offline, keeping everything local and private

🛠️ Getting Started

1. Grab the Code

Clone or download the project to your machine:

```bash
git clone https://github.com/Aharamsahithi13/reddit-persona-generator.git
cd reddit-persona-generator
```

2. Install Python Packages

Set up the required libraries:

```bash
pip install -r requirements.txt
```

What you’ll need:
- `praw`: For accessing Reddit’s API
- `python-dotenv`: For securely handling environment variables

3. Set Up Reddit API Access

Create a `.env` file in the project folder and add your Reddit API credentials:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=reddit_persona_script by u/your_username
```

> 🔐 Tip: Get your Reddit API credentials by creating an app at [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).

4. Install Ollama and the `phi` Model

- Download Ollama from [https://ollama.com/download](https://ollama.com/download).
- Run this command once to set up the `phi` model:

```bash
ollama run phi
```

---

▶️ How to Use It

Launch the script:

```bash
python persona_generator_phi.py
```

When prompted, paste a Reddit user’s profile URL, like:

```
🔗 Enter Reddit user profile URL: https://www.reddit.com/user/Hungry-Move-6603/
```

The script will analyze the user’s activity and save the persona to the `outputs/` folder.

📁 Output Details

- Format: Plain text (`.txt`)
- Location: `outputs/<username>_persona.txt`

The persona includes:
- 🧠 Persona Overview: A quick snapshot of the user
- 🔸 Summary: A short paragraph about their vibe
- 🌱 Interests & Hobbies: What they’re into
- 🗣️ Communication Style: How they express themselves
- 📌 Common Themes: Recurring topics in their posts/comments
- 📎 Citations: Links to real Reddit posts/comments for reference

---

📄 Example Output

```
🧠 USER PERSONA: u/Hungry-Move-6603

🔸 Summary
This user is vocal about local issues, food experiences, and civic matters, often with a sharp, candid tone.

🌱 Interests & Hobbies
Loves discussing city life, food quality, and social dynamics.
- Switched to cooking power meals at home...
  Source: https://www.reddit.com/r/lucknow/comments/...

🗣️ Communication Style
Bold, sarcastic, and straight to the point.
- Got any tough friends or big siblings to back you up?
  Source: https://www.reddit.com/r/indiasocial/comments/...

📌 Common Themes
City governance, traffic woes, food gripes, and bribery concerns.
- Cops always have a sidekick to negotiate bribes.
  Source: https://www.reddit.com/r/nagpur/comments/...

📎 Citations
1. https://www.reddit.com/r/lucknow/comments/...
2. https://www.reddit.com/r/indiasocial/comments/...
3. https://www.reddit.com/r/nagpur/comments/...
```

📦 Project Structure

```
reddit-persona-generator/
├── persona_generator.py  # Core script
├── requirements.txt          # Python dependencies
├── .env                     # Reddit API credentials (create this)
├── outputs/                 # Where personas are saved
└── README.md                # You’re reading it!
```

✅ Shoutouts

- Reddit data pulled using [PRAW](https://praw.readthedocs.io/)
- Local AI magic by [Ollama](https://ollama.com/) with the `phi` model
- `phi`: A fast, open-source model for lightweight inference

📌 License

MIT License. Feel free to use, tweak, or share this project. A nod to the creator is always appreciated!
