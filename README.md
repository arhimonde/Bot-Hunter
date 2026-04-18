# 🚀 Global Deal Hunter 70% (Bot Hunter)

A powerful, multi-sector web scraper designed to catch "Super Deals" (70% discount or higher) from major aggregators and stores. The bot monitors price drops in real-time and sends instant notifications to your Telegram.

## 🌟 Key Features
- **Global Coverage**: Scans massive deal aggregators (like Chollometro) covering Amazon, eBay, MediaMarkt, and more.
- **Smart Filtering**: Only notifies you if a deal has a **70% discount** or higher.
- **Rich Notifications**: Includes price, savings percentage, time posted, expiry info, and direct links.
- **Stealth Mode**: Uses advanced Selenium techniques to bypass bot detection.

---

## 🛠️ Installation (PC)

### 1. Requirements
Ensure you have **Python 3.9+** and **Google Chrome** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/arhimonde/Bot-Hunter.git
cd Bot-Hunter
```

### 3. Install Dependencies
```bash
pip3 install -r requirements.txt
```

---

## 📱 Telegram Setup (Phone/PC)

To receive alerts on your phone, you need to create a Telegram Bot:

1. **Get Bot Token**:
   - Open Telegram and search for **@BotFather**.
   - Send `/newbot` and follow the instructions to get your **API Token**.
2. **Get Your Chat ID**:
   - Search for **@userinfobot** on Telegram.
   - Press **Start**. It will give you your numeric **Id** (e.g., `6248809747`).
3. **Start the Conversation**:
   - Go to your newly created bot and press **START**.

---

## ⚙️ Configuration

1. Create a file named `.env` in the project root (if not already present).
2. Fill in your credentials:
   ```env
   TELEGRAM_BOT_TOKEN=your_token_here
   TELEGRAM_CHAT_ID=your_id_here
   ```
3. (Optional) Customize categories in `trackers.json`.

---

## 🚀 How to Run

Start the bot by running the following command in your terminal:

```bash
python3 main.py
```

### What happens next?
- The bot will send a **Welcome Message** to your Telegram to confirm it's working.
- It will perform an immediate scan of all configured sectors.
- It will continue scanning every **1 hour** in the background.
- You will receive a notification **ONLY** when a 70%+ deal is detected.

---

## 🛡️ Security Note
The `.env` file is included in `.gitignore` to ensure your private tokens are NEVER uploaded to public repositories. **Keep your tokens secret!**

---
*Created with ❤️ by Antigravity for arhimonde.*
