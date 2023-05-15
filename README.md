# Outlook Generator

Outlook Generator is an automation tool that creates Outlook accounts and stores the email addresses and passwords of the generated accounts. This project leverages Selenium for web automation, the Nopecha extension to solve CAPTCHAs, and WireGuard to bypass IP limitations.

# NOPECHA SEEMS TO BE PATCHED ON OUTLOOK CURRENTLY!

## Getting Started

1. Clone the repository: `git clone https://github.com/kaajjaak/OutlookGenerator.git`

2. Install the required packages: `pip install -r requirements.txt`

3. Install [WireGuard](https://www.wireguard.com/install/) for your device and ensure that the wireguard executable is added to PATH (or equivalent on your OS).

6. Adding WireGuard config files: The program passes the config files to WireGuard, it looks for them in a folder called `./wireguard_configs` (starting from the project root). Create this folder and put your config files in it, I generated mine for Mullvad from the [WireGuard configuration file generator](https://mullvad.net/en/account/#/wireguard-config/?platform=windows). I have only tested this project using Mullvad WireGuard configs so I cannot guarantee it will work with any other WireGuard providers.

5. Configure the settings: rename the .env.template file to .env and fill in the [NopeCha API key](https://nopecha.com/manage) and settings URL which you can get from inside of the extension.
(alternatively you can compile your own .crx file of the beta version with your settings key configured in the manifest.json file and make some minor changes to the code)

## Deployment

Run the main.py file in Administrator (or sudo on Linux), this is required to interact with the WireGuard executable, you could change the executable permissions but I would personally suggest not to do that.

## Author

- [@Akina](https://www.github.com/kaajjaak)
