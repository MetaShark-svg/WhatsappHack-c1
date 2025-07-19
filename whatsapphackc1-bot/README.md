# WhatsAppHackC1Bot

This Telegram bot automates payment verification and access control for the private WhatsApp hack tool repository.

## 💡 Features

- `/start` — Welcome message
- `/buy` — Shows ETH payment instructions
- `/access` — Verifies payment to access repo
- `/status` — Shows bot uptime status
- `/help` — Help & support info

## 💰 Payment Info

- **Amount**: `0.25 ETH`
- **Address**: `0xb58937eB4D98E79e66522D32DDc6a4004ed74Ae9`
- **Telegram**: [@cyberleaklod](https://t.me/cyberleaklod)

---

## 🔧 Deploy Instructions

1. Clone or unzip this repo.
2. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run it manually:
   ```bash
   python3 whatsapp_bot.py
   ```

4. Or install as a service:

### 🛠️ systemd Service Setup

Create a service file:

```bash
sudo nano /etc/systemd/system/whatsappbot.service
```

Paste:

```ini
[Unit]
Description=WhatsAppHackC1Bot Telegram Bot
After=network.target

[Service]
ExecStart=/full/path/to/venv/bin/python3 /full/path/to/whatsapp_bot.py
WorkingDirectory=/full/path/to
Restart=always
User=yourusername

[Install]
WantedBy=multi-user.target
```

Reload and start service:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable whatsappbot
sudo systemctl start whatsappbot
```
