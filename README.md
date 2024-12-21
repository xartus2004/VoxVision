# VoxVision: Discord Bot for Generating Images with Prodia API

VoxVision is a Python-based Discord bot that leverages Prodia's powerful image generation API to create stunning visuals directly from Discord. This bot provides an easy and scalable way to integrate AI-powered image generation into your server.

---

## 🚀 Getting Started

### Open Using Daytona

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/) to set up Daytona.

2. **Start the Server**:
   ```bash
   daytona serve;
   ```

3. **Create the Workspace**:
   ```bash
   daytona create https://github.com/xartus2004/VoxVision
   ```

4. **Setup Environment**:  
   Install all necessary dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the Bot**:

   - Create a `.env` file in the root of the project and add your Discord bot token and Prodia API key:
     ```
     DISCORD_TOKEN=your_discord_bot_token
     PRODIA_API_KEY=your_prodia_api_key
     ```

6. **Run the Bot**:  
   Start the bot by executing the following command:
   ```bash
   python bot.py
   ```

---

## ✨ Features

- **Integration with Daytona**: Development environment standardized with devcontainers for consistency.
- **Modular Design**: Easy to extend with more features or commands.
- **Discord API**: Facilitates interaction in real-time on Discord servers.
- **Prodia API Integration**: Generate images on-demand by sending text prompts.
- **Customizable Commands**: Add your own commands or adjust existing ones to suit your needs.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

---

## 📜 License

This repository is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 📚 Learn More

For more details on Daytona, visit the [official documentation](https://www.daytona.io/docs).

For information on the Prodia API, check their [documentation](https://prodia.com/docs).

---

Let me know if you'd like to add or modify any sections!