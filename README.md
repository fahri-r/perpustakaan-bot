<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
![Repo Size][size-shield]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/fahri-r/perpustakaan-bot">
    <img src="https://drive.google.com/uc?id=1QNUs6MW3SocMNyNDWVFguI4fW7TEa1ml" alt="Logo" height="80">
  </a>

<h3 align="center">Perpustakaan Telegram Bot</h3>

  <p align="center">
     Telegram bot for library management system.
    <br />
    <a href="https://github.com/fahri-r/perpustakaan-bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://t.me/PerpustakaankuBot">View Demo</a>
    ·
    <a href="https://github.com/fahri-r/perpustakaan-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/fahri-r/perpustakaan-bot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

Perpustakaan Telegram Bot (Library) is telegram bot for library management system. It can manage member data in a library. This bot consumes [Perpustakaan API](https://github.com/fahri-r/perpustakaan-api).

<p align="right">
    <a href="#top">
    <img src="https://img.shields.io/badge/back%20to%20top-%E2%86%A9-blue" />
    </a>
</p>


### Built With

* [Python](https://www.python.org/)
* [python-telegram-bot](https://python-telegram-bot.org/)

<p align="right">
    <a href="#top">
    <img src="https://img.shields.io/badge/back%20to%20top-%E2%86%A9-blue" />
    </a>
</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [Python v3.9.8 or higher](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/fahri-r/perpustakaan-bot.git
   ```

2. Install Python packages.
   ```sh
   pip install -r requirements.txt
   ```

3. Rename `.env.example` into `.env`.

4. Set `BOT_TOKEN` value in `.env` (you can get the token from [BotFather](https://t.me/BotFather)).
   ```sh
   ...
   BOT_TOKEN=
   ...
   ```

<p align="right">
    <a href="#top">
    <img src="https://img.shields.io/badge/back%20to%20top-%E2%86%A9-blue" />
    </a>
</p>



<!-- USAGE EXAMPLES -->
## Usage

### Start on the local server

1. Open `main.py` and uncomment this line.
   ```
   ...
   # updater.start_polling() 
   ...
   ```

2. Also comment this line.
   ```
   ...
   updater.start_webhook(listen=HOST,
                         port=int(PORT),
                         url_path=TOKEN,
                         webhook_url=URL_APP + TOKEN)
   ...
   ```

3. Run main.py.
   ```
   python main.py
   ```

### Deployment

When you're ready to deploy this bot into production, you have to change `URL_APP` value in `.env`. The value must be the url where the bot is deployed.

<p align="right">
    <a href="#top">
    <img src="https://img.shields.io/badge/back%20to%20top-%E2%86%A9-blue" />
    </a>
</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">
    <a href="#top">
    <img src="https://img.shields.io/badge/back%20to%20top-%E2%86%A9-blue" />
    </a>
</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">
    <a href="#top">
    <img src="https://img.shields.io/badge/back%20to%20top-%E2%86%A9-blue" />
    </a>
</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/fahri-r/perpustakaan-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/fahri-r/perpustakaan-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/fahri-r/perpustakaan-bot.svg?style=for-the-badge
[forks-url]: https://github.com/fahri-r/perpustakaan-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/fahri-r/perpustakaan-bot.svg?style=for-the-badge
[stars-url]: https://github.com/fahri-r/perpustakaan-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/fahri-r/perpustakaan-bot.svg?style=for-the-badge
[issues-url]: https://github.com/fahri-r/perpustakaan-bot/issues
[license-shield]: https://img.shields.io/github/license/fahri-r/perpustakaan-bot.svg?style=for-the-badge
[license-url]: https://github.com/fahri-r/perpustakaan-bot/blob/master/LICENSE
[size-shield]: https://img.shields.io/github/repo-size/fahri-r/perpustakaan-bot.svg?style=for-the-badge
[product-screenshot]: https://drive.google.com/uc?id=1rT1HApQ4Xi1tH_ot72rwNPL5WCeeVG1e