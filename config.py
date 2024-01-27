import configparser
from colorama import Fore
import os

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'
github = 'https://github.com/spyboy-productions/CloakQuest3r'

VERSION = '1.0.4'

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow


def read_config():
    config = configparser.ConfigParser()

    if not os.path.exists('config.ini'):
        config["DEFAULT"] = {
            "securitytrails_api_key": "your_api_key"}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print(f"\n[!] {Fore.RED}Please add your {C}SecurityTrails{Fore.RED} API Key in config.ini file{Fore.RESET}")
    else:
        config.read('config.ini')
        APIKEY = config['DEFAULT']['securitytrails_api_key']
        return APIKEY


def generate_random_ua():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    return user_agent_rotator.get_random_user_agent()