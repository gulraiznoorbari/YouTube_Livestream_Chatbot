# YouTube Live Stream Chatbot

### This Chat Bot was developed using YouTube Data & Live Streaming API v3 in Python

The bot replies to live chat messages in a Live Stream (obviously :p). It currently has a limited set of commands to respond to, but you can easily add more.

## ⬇️ How to setup

1. Goto [Google Developers Console](https://console.developers.google.com/) and create a new project.

2. Enable YouTube Data API v3
3. Then from the Credentials tab, create a new OAuth Client ID and select the Web Application option. In the "Authorized redirect URIs" section, add the redirect URI you want to use. In the case of this project you will type "http://localhost:5500/" (you can use any port but I am specifically using 5500 as I have declared that as my auth uri in the auth.py script) and click Save.
4. Create a `.env` file in your project directory and copy/paste the Client ID and Client Secret in the file.
5. Then Copy & Paste the following commands in your terminal:

```
git clone https://github.com/gulraiznoorbari/YouTube_Live_Stream_Chat_Bot.git
cd YouTube_Live_Stream_Chat_Bot
python bot.py
```

The bot will ask you to authenticate yourself with your Google Account.

After that, you will be prompted to enter a Live Stream Id in you terminal:

> www.youtube.com/watch?v=qDWw4sAD3zY

Here, the Live Stream Id is **`qDWw4sAD3zY`**

## 👨‍💻 Author

You can get in touch with me on my LinkedIn Profile:

#### Gulraiz Noor Bari

[![LinkedIn Link](https://img.shields.io/badge/Connect-gulraiznoorbari-blue.svg?logo=linkedin&longCache=true&style=social&label=Connect)](https://www.linkedin.com/in/gulraiznoorbari)
<br />
You can also follow my GitHub Profile to stay updated about my latest projects: [![GitHub Follow](https://img.shields.io/badge/Connect-gulraiznoorbari-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/gulraiznoorbari)

If you liked the repo then kindly support it by giving it a star ⭐!

## Contributions Welcome

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](#)

If you find any bug in the code or have any improvements in mind then feel free to generate a pull request.
