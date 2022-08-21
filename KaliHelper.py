#CODE BY L1B3RTAS 21.08.2022
import fade
import os
from colorama import Fore, Back, Style
import netifaces
import pathlib
from random import randint
import urllib.request
import socket
import threading
import telebot
from color import *
from token1 import *
from time import sleep
main = ("""
██╗  ██╗ █████╗ ██╗     ██╗    ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██║ ██╔╝██╔══██╗██║     ██║    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
█████╔╝ ███████║██║     ██║    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██╔═██╗ ██╔══██║██║     ██║    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██╗██║  ██║███████╗██║    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝   
                                               By l1b3rtaS   V0.7
					MENU
	1. Update and upgrade all apt library (required to use other functions)
	2. Best Tools from GitHub
	3. Popular programs
	4. Download BrootLists Pack    
	5. Local SSH start
	6. Neofetch
	7. 2vol.msg (P2P Chatting)
	8. File-saver bot (TG)
	9. Cap file Bruteforce

	99. Exit

	Choose:                                                                           
 """)
faded_main = fade.purplepink(main)
github = ("""

 ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║
╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
					ALL TOOLS  
	1. GoldenEye (DoS)
	2. Storm-Breaker (Deanon Multi-Tool)
	3. Zphisher (30 Fast-Setup Fishing sites)
	4.
	5. ProxyGen (ProxyList generator)

	99. Exit

	Choose:
""")                                                                         
faded_github = fade.purpleblue(github)
popru = ("""
██████╗  ██████╗ ██████╗ ██╗   ██╗██╗      █████╗ ██████╗     ██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██╔═══██╗██╔══██╗██║   ██║██║     ██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔════╝
██████╔╝██║   ██║██████╔╝██║   ██║██║     ███████║██████╔╝    ██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║███████╗
██╔═══╝ ██║   ██║██╔═══╝ ██║   ██║██║     ██╔══██║██╔══██╗    ██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║╚════██║
██║     ╚██████╔╝██║     ╚██████╔╝███████╗██║  ██║██║  ██║    ██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║███████║
╚═╝      ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
					PROGRAMS AUTO-INSTALLER
	1. Spotify
	2. Sublime Text
	3. Telegram
	4. Tor Browser
	5. Router Scan
	6. qBittorrent
	7. mat2 (Metadata-Cleaner)
	8. Discord
	9. Steam

	99. Exit

	Choose:
""")
faded_popru = fade.fire(popru)
vvm = ("""
██████╗ ██╗   ██╗ ██████╗ ██╗        ███╗   ███╗███████╗ ██████╗ 
╚════██╗██║   ██║██╔═══██╗██║        ████╗ ████║██╔════╝██╔════╝ 
 █████╔╝██║   ██║██║   ██║██║        ██╔████╔██║███████╗██║  ███╗
██╔═══╝ ╚██╗ ██╔╝██║   ██║██║        ██║╚██╔╝██║╚════██║██║   ██║
███████╗ ╚████╔╝ ╚██████╔╝███████╗██╗██║ ╚═╝ ██║███████║╚██████╔╝
╚══════╝  ╚═══╝   ╚═════╝ ╚══════╝╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝                                                               
                              P2P CHATTING
    
    If you start NetCat first time launch "3. Config", 
    for set nickname and color

    1. Start session
    2. Join session
    3. Config

    99. Exit

    Choose:
""")
faded_2vm = fade.greenblue(vvm)
vm = ("""
██████╗ ██╗   ██╗ ██████╗ ██╗        ███╗   ███╗███████╗ ██████╗ 
╚════██╗██║   ██║██╔═══██╗██║        ████╗ ████║██╔════╝██╔════╝ 
 █████╔╝██║   ██║██║   ██║██║        ██╔████╔██║███████╗██║  ███╗
██╔═══╝ ╚██╗ ██╔╝██║   ██║██║        ██║╚██╔╝██║╚════██║██║   ██║
███████╗ ╚████╔╝ ╚██████╔╝███████╗██╗██║ ╚═╝ ██║███████║╚██████╔╝
╚══════╝  ╚═══╝   ╚═════╝ ╚══════╝╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝                                                                
                              P2P CHATTING

""")
faded_vm = fade.greenblue(vm)
psb = ("""
████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗    ███████╗ █████╗ ██╗   ██╗███████╗██████╗     ██████╗  ██████╗ ████████╗
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║    ███████╗███████║██║   ██║█████╗  ██████╔╝    ██████╔╝██║   ██║   ██║   
   ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║    ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██╔══██╗██║   ██║   ██║   
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    ███████║██║  ██║ ╚████╔╝ ███████╗██║  ██║    ██████╔╝╚██████╔╝   ██║   
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝
				Telegram Bot that saves sent files to your PC
""")
faded_psb = fade.pinkred(psb)
cbf = ("""
 ██████╗ █████╗ ██████╗     ██████╗ ██████╗ ██╗   ██╗████████╗███████╗      ███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝      ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██║     ███████║██████╔╝    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ████  █████╗  ██║   ██║██████╔╝██║     █████╗  
██║     ██╔══██║██╔═══╝     ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝        ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
╚██████╗██║  ██║██║         ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗      ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝         ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
 				Broot-force cap files using aircrack
 			Cap file and Brute List must be in KaliHelper folder
 					For exit press Ctrl+C
""")
faded_cbf = fade.brazil(cbf)
#EMOJI
ohfuck = Fore.BLACK + Back.WHITE + """凸(▼ｪ▼ﾒ)""" + Style.RESET_ALL
angry = Fore.BLACK + Back.WHITE + """(╬◣益◢)""" + Style.RESET_ALL
wow = Fore.BLACK + Back.WHITE + """╚╚|░☀▄☀░|╝╝""" + Style.RESET_ALL
um = Fore.BLACK + Back.WHITE + """(°ʖ°)""" + Style.RESET_ALL
damn = Fore.BLACK + Back.WHITE + """【•】_【•】""" + Style.RESET_ALL
uh = Fore.BLACK + Back.WHITE + """./((-＿-メ))\.""" + Style.RESET_ALL
idk = Fore.BLACK + Back.WHITE + """¯\_( ° ʖ °͠)_/¯""" + Style.RESET_ALL
sad = Fore.BLACK + Back.WHITE + """੨( ･᷄ ︵･᷅ )ｼ""" + Style.RESET_ALL
dance = Fore.BLACK + Back.WHITE + """((┌|o^▽^o|┘))♪""" + Style.RESET_ALL
def ip():
    return urllib.request.urlopen('http://ip-address.ru/show').read().decode('utf-8')
a = 1
while a == 1:
	os.system("clear")
	print(faded_main)
	choose = input()
	if choose == "1":
		os.system("sudo apt --fix-broken install -y")
		os.system("sudo apt upgrade -y && apt update -y")
		os.system("sudo apt install git -y")
		os.system("sudo apt install python3 -y")
		os.system("sudo apt install wordlists -y")
		os.system("sudo apt install neofetch -y")
		os.system("sudo apt-get install p7zip-full -y")
		os.system("sudo apt install wine -y")
		os.system("apt-get install wine32 -y")
		os.system("sudo apt install netcat-openbsd -y")
		input(Fore.MAGENTA + "Press enter for continue" + Fore.WHITE)
	if choose == "2":
		b = 1
		while b == 1:	
			os.system("clear")
			print(faded_github)
			choose_git = input()
			if choose_git == "1":
				os.system("git clone https://github.com/jseidl/GoldenEye")
				print (Fore.BLUE + """
	Site (Full instruction) - https://github.com/jseidl/GoldenEye
					
	For use , exit KaliHelper , choose derictory to KaliHelper/GoldenEye and send command 
	./goldeneye <url> 
					""")
				input(Fore.BLUE + "Press enter for continue" + Fore.WHITE)
			if choose_git == "2":
				os.system("git clone https://github.com/ultrasecurity/Storm-Breaker")
				print (Fore.BLUE + """
	Site (Full instruction) - https://github.com/ultrasecurity/Storm-Breaker
					
	For use , exit KaliHelper , choose derictory to KaliHelper/Storm-Breaker and follow instructions from GitHub
					""")
				input(Fore.BLUE + "Press enter for continue" + Fore.WHITE)
			if choose_git == "3":
				os.system("git clone https://github.com/htr-tech/zphisher")
				print (Fore.BLUE + """
	Site (Full instruction) - https://github.com/htr-tech/zphisher

	For use , exit KaliHelper , choose derictory to KaliHelper/zphisher and send command 
	bash zphisher.sh
					""")
				input(Fore.BLUE + "Press enter for continue" + Fore.WHITE)
			if choose_git == "5":
				os.system("git clone https://github.com/l1b3rtaS/ProxyGen")
				print (Fore.BLUE + """
	Site (Full instruction) - https://github.com/l1b3rtaS/ProxyGen

	For use , exit KaliHelper , choose derictory to KaliHelper/ProxyGen and send command
	python ProxyGen.py
					""")
				input(Fore.BLUE + "Press enter for continue" + Fore.WHITE)
			if choose_git == "99":
				b = 2
	if choose == "3":
		c = 1
		while c == 1:
			os.system("clear")
			print(faded_popru)
			choose_programs = input()
			if choose_programs == "1":
				print (Fore.RED + """
					Spotify Download Started
					""" + Fore.WHITE)
				os.system("curl -sS https://download.spotify.com/debian/pubkey_5E3C45D7B312C643.gpg | sudo apt-key add -")
				os.system('echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list')
				os.system("sudo apt-get update -y && sudo apt-get install spotify-client -y")
				print (Fore.RED + """
					Spotify Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue" + Fore.WHITE)
			if choose_programs == "2":
				print (Fore.RED + """
					Sublime Text Download Started
					""" + Fore.WHITE)
				os.system('sudo wget -O sublimetext.deb "https://download.sublimetext.com/sublime-text_build-3211_amd64.deb"')
				os.system("sudo dpkg -i sublimetext.deb")
				os.system("sudo rm sublimetext.deb")
				print (Fore.RED + """
					Sublime Text Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue" + Fore.WHITE)
			if choose_programs == "3":
				print (Fore.RED + """
					Telegram Download Started
					""" + Fore.WHITE)
				os.system("sudo apt install telegram-desktop -y")
				print (Fore.RED + """
					Telegram Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue" + Fore.WHITE)
			if choose_programs == "4":
				print (Fore.RED + """
					Tor Browser Download Started
					""" + Fore.WHITE)
				os.system("sudo apt install torbrowser-launcher -y")
				print (Fore.RED + """
					Tor Browser Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue" + Fore.WHITE)
			if choose_programs == "5":
				print (Fore.RED + """
					Router Scan Download Started
					""" + Fore.WHITE)
				os.system("dpkg --add-architecture i386 && apt-get update && apt-get install wine32:i386")
				os.system("gdown https://drive.google.com/uc?id=1yKPVTggfyCeQmhRXmKkqiXAJaAk38OAX")
				os.system("7z x rs.zip -aoa -pl1b3rtaS -oRouterScan")
				print (Fore.RED + """
					Router Scan Download completed

					For launch Router scan , exit KaliHelper and send this commands:
					cd RouterScan
					wine RouterScan.exe
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue" + Fore.WHITE)
			if choose_programs == "6":
				print (Fore.RED + """
					qBittorrent Download Started
					""" + Fore.WHITE)
				os.system("sudo apt install qbittorrent -y")
				print (Fore.RED + """
					qBittorrent Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue" + Fore.WHITE)
			if choose_programs == "7":
				print (Fore.RED + """
					Mat2 (Metadata-Cleaner) Download Started
					""" + Fore.WHITE)
				os.system("sudo apt install mat2 -y")
				os.system("sudo apt install metadata-cleaner -y")
				print (Fore.RED + """
					Mat2 (Metadata-Cleaner) Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue" + Fore.WHITE)
			if choose_programs == "8":
				print (Fore.RED + """
					Discord Download Started
					""" + Fore.WHITE)
				os.system('sudo wget -O discord.deb "https://discordapp.com/api/download?platform=linux&format=deb"')
				os.system("sudo dpkg -i discord.deb")
				os.system("sudo rm discord.deb")
				print (Fore.RED + """
					Discord Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue")
			if choose_programs == "9":
				print (Fore.RED + """
					Steam Download Started
					""" + Fore.WHITE)
				os.system('sudo wget -O steam.deb "https://cdn.akamai.steamstatic.com/client/installer/steam.deb"')
				os.system("sudo dpkg -i steam.deb")
				os.system("rm steam.deb")
				print (Fore.RED + """
					Steam Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue" + Fore.WHITE)
			if choose_programs == "99":
				c = 2
	if choose == "4":
		print(Fore.GREEN + """
					BrootLists Pack (Zip-850Mb) Download Started 
			""")   
		os.system("gdown https://drive.google.com/uc?id=1gqbNRYthRPvox3x7oG059AsMn5-YHxdW")
		print("""
					BrootLists Pack Download Done 
					It is located in the KaliHelper folder
					After unzipping the brootlists will weigh 3.9Gb
			"""+Fore.WHITE)
		
		input(Fore.GREEN + "Press enter for continue" + Fore.WHITE)
	if choose == "5":
		print (Fore.MAGENTA + """		Your local IPs , for SSH conect use IP who started 192.168
			""")
		interfaces_list = netifaces.interfaces()
		max_amount = len(interfaces_list)
		number = 0
		attemps = 0
		while attemps < max_amount:
			t = (interfaces_list[number]) 
			ipint = netifaces.ifaddresses(t)[netifaces.AF_INET][0]['addr']
			print ("				" + ipint)
			number = number + 1
			attemps = attemps + 1
		os.system("sudo systemctl start ssh.socket")
		print (Fore.MAGENTA + """


			
				SSH STARTED
		
		For connect - open Terminal on your Phone or Computer and type command
		ssh USER@HOSTLOCALIP
				""" + Fore.WHITE)
		input(Fore.MAGENTA + "Press enter for continue" + Fore.WHITE)	
	if choose == "6":
		os.system("clear")
		os.system("neofetch")
		input(Fore.CYAN + "Press enter for continue" + Fore.WHITE)	
	if choose == "7":
		d = 1
		while d == 1:	
			os.system("clear")
			print(faded_2vm)
			choose_nct = input()
			if choose_nct == "1":			
				print (Fore.MAGENTA + """		Your local IPs , for hosting connect type IP who started 192.168
			""")
				interfaces_list = netifaces.interfaces()
				max_amount = len(interfaces_list)
				number = 0
				attemps = 0
				while attemps < max_amount:
					t = (interfaces_list[number]) 
					ipint = netifaces.ifaddresses(t)[netifaces.AF_INET][0]['addr']
					print ("				" + ipint)
					number = number + 1
					attemps = attemps + 1
				print(Fore.WHITE)
				UDP_MAX_SIZE = 65535
				lip = input()
				def listen(host: str = lip , port: int = 1337):
				    server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
				    server.bind((host , port))
				    print(Fore.CYAN + '			Listeting at ' + host + ':' + str(port) + Fore.WHITE)
				    print(Fore.CYAN + '			   CHAT-SERVER STARTED ' + Fore.WHITE)
				    members = []
				    while True:
				        msg , addr = server.recvfrom(UDP_MAX_SIZE)
				        if addr not in members:
				            members.append(addr)
				        if not msg:
				            continue
				        client_id = addr[1]
				        if msg.decode('utf-8') == '__join':
				            print(f'SERVER> Client {client_id} joined chat') 
				            continue
				        print('\r\r' + msg.decode('utf-8'))
				        msg = f'{msg.decode("utf-8")}'
				        for member in members:
				            if member == addr:
				                continue
				            server.sendto(msg.encode('utf-8') , member)
				if __name__ == '__main__':
					os.system("clear")
					print(faded_vm)
					print(Fore.CYAN + """            			Server Start
	For sombody join , he need to choose 2. Join in KaliHelper-P2PCHAT 
	  For you (server starter) join , you need to launch another one 
	        Kali Helper and choose 2. Join in Kali Helper-P2PCHAT 
If you have [Errno 98] Address already in use , exit Kali Helper and send command
	  		sudo kill -9 $(lsof -t -i:1337)

			   For exit press Ctrl+C""" + Fore.WHITE)
					listen()
			if choose_nct == "2":
				nickf = open("nick.txt", "r")
				nick = nickf.read()
				nccolor = color
				nickname = nccolor + nick + Fore.WHITE
				UPD_MAX_SIZE = 65535
				print (Fore.MAGENTA + """		Enter hoster IP , started at 192.168
			""" + Fore.WHITE)
				lipu = input()
				def listen(server: socket.socket):
				    while True:
				        msg = server.recv(UPD_MAX_SIZE)
				        print('\r\r' + msg.decode('utf-8') + '\n' + f'you: ' , end='')
				def connect(host: str = lipu , port: int = 1337):
				    server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
				    server.connect((host,port))
				    threading.Thread(target=listen, args=(server,), daemon=True).start()
				    server.send('__join'.encode('utf-8'))
				    while True:
				        sw = 1
				        msg1 = input(f'you: ')
				        if msg1 == ".emjlist":
				        	print (Fore.CYAN + """To send a emoji send the command in a separate message 
(Emoji is visible only to other members)
Emoji List:
				        		""")
				        	print(Fore.CYAN + ".ohfuck  -  " + ohfuck)
				        	print(Fore.CYAN + ".angry  -  " + angry)
				        	print(Fore.CYAN + ".wow  -  " + wow)
				        	print(Fore.CYAN + ".um  -  " + um)
				        	print(Fore.CYAN + ".damn  -  " + damn)
				        	print(Fore.CYAN + ".uh  -  " + uh)
				        	print(Fore.CYAN + ".idk  -  " + idk)
				        	print(Fore.CYAN + ".sad  -  " + sad)
				        	print(Fore.CYAN + ".dance  -  " + dance + Fore.WHITE)
				        	sw = 2
				        if msg1 == ".ohfuck":
				        	msg = (nickname +  " " + ohfuck) 
					        server.send(msg.encode('utf-8'))
					        sw = 2	
				        if msg1 == ".angry":
				        	msg = (nickname +  " " + angry) 
				        	server.send(msg.encode('utf-8'))
				        	sw = 2
				        if msg1 == ".wow":
				        	msg = (nickname +  " " + wow) 
				        	server.send(msg.encode('utf-8'))
				        	sw = 2
				        if msg1 == ".um":
				        	msg = (nickname +  " " + um) 
				        	server.send(msg.encode('utf-8'))
				        	sw = 2
				        if msg1 == ".damn":
				        	msg = (nickname +  " " + damn) 
				        	server.send(msg.encode('utf-8'))
				        	sw = 2
				        if msg1 == ".uh":
				        	msg = (nickname +  " " + uh) 
				        	server.send(msg.encode('utf-8'))
				        	sw = 2
				        if msg1 == ".idk":
				        	msg = (nickname +  " " + idk) 
				        	server.send(msg.encode('utf-8'))
				        	sw = 2
				        if msg1 == ".sad":
				        	msg = (nickname +  " " + sad) 
				        	server.send(msg.encode('utf-8'))
				        	sw = 2
				        if msg1 == ".dance":
				        	msg = (nickname +  " " + dance) 
				        	server.send(msg.encode('utf-8'))
				        	sw = 2
				        if sw == 1:
					        msg = (nickname +  " " + msg1) 
					        server.send(msg.encode('utf-8'))			    
				if __name__ == '__main__':
				    os.system("clear")
				    print(faded_vm)
				    print(f"""
		{nickname + Fore.CYAN} , welcome to chat  
	your nick and color visible for other members
		See list of emoji - .emjlist
		For exit press Ctrl+C""" + Fore.WHITE)
				    connect()
			if choose_nct == "3":
				e = 1
				while e == 1:
					os.system("clear")
					print(faded_vm)
					print(Fore.CYAN + """
	NETCAT CONFIG

	Changes apply only after reload Kali Helper

	1. Set nickname
	2. Set nickname Color

	99. Exit

	Choose:
""" + Fore.WHITE)
					choose_ncf = input()
					if choose_ncf == "1":
						h = 1
						while h == 1:
							os.system("clear")
							print(faded_vm)	
							print(Fore.CYAN + """
		1. Enter new nickname

		99. Exit
	""" + Fore.WHITE)
							newnickc = input()
							if newnickc == "1":
								print(Fore.CYAN + """Type your new nickname
									""" + Fore.WHITE)
								new_nick1 = input()
								nick_file = open("nick.txt", "w") 
								nick_file.write(str(new_nick1))
							if newnickc == "99":
								h = 2
					if choose_ncf == "2":
						g = 1
						while g == 1:
							os.system("clear")
							print(faded_vm)			
							print(Fore.CYAN + """
		Choose new nickname color
	""")
							print("""
		1. """ + Fore.BLACK + """Black""" + Fore.CYAN + """
		2. """ + Fore.RED + """Red""" + Fore.CYAN + """
		3. """ + Fore.GREEN + """Green""" + Fore.CYAN + """
		4. """ + Fore.YELLOW + """Yellow""" + Fore.CYAN + """
		5. """ + Fore.BLUE + """Blue""" + Fore.CYAN + """
		6. """ + Fore.MAGENTA + """Purple""" + Fore.CYAN + """
		7. """ + Fore.CYAN + """Cyan""" + Fore.CYAN + """
		8. """ + Fore.WHITE + """White""" + Fore.CYAN + """

		99. Exit
	""")
							new_color = input()
							color_file = open("color.py", "w") 
							if new_color == "1":
								color_file.write("from colorama import Fore, Back, Style \n" + "color = Fore.BLACK")
							if new_color == "2":
								color_file.write("from colorama import Fore, Back, Style \n" + "color = Fore.RED")
							if new_color == "3":
								color_file.write("from colorama import Fore, Back, Style \n" + "color = Fore.GREEN")
							if new_color == "4":
								color_file.write("from colorama import Fore, Back, Style \n" + "color = Fore.YELLOW")
							if new_color == "5":
								color_file.write("from colorama import Fore, Back, Style \n" + "color = Fore.BLUE")
							if new_color == "6":
								color_file.write("from colorama import Fore, Back, Style \n" + "color = Fore.MAGENTA")
							if new_color == "7":
								color_file.write("from colorama import Fore, Back, Style \n" + "color = Fore.CYAN")
							if new_color == "8":
								color_file.write("from colorama import Fore, Back, Style \n" + "color = Fore.WHITE")
							if new_color == "99":
								g = 2	
					if choose_ncf == "99":
						e = 2
			if choose_nct == "99":
				d = 2
	if choose == "8":
		m = 1
		while m == 1:	
			os.system("clear")
			print(faded_psb)
			if TOKEN1 == "None":
				ts = Fore.WHITE + "[" + Fore.RED + "TOKEN NOT SET" + Fore.WHITE + "]"
			else:
				ts = Fore.WHITE + "[" + Fore.GREEN + "TOKEN SET" + Fore.WHITE + "]"
			print(Style.BRIGHT + Fore.MAGENTA + "	If the bot does not start, check the validity of the token\n\n" + "	1. Start Bot\n""" + "	2. Set token " + Style.RESET_ALL + ts + "\n\n" + Style.BRIGHT + Fore.MAGENTA + "	99. Exit")
			choose_psb = input()
			if choose_psb == "1":
				os.system("clear")
				print(faded_psb)
				print(Style.BRIGHT + Fore.MAGENTA + "\n 		To work, write to the bot /start\n			Press Ctrl+C to stop\n" + Style.RESET_ALL)
				bot = telebot.TeleBot(TOKEN1)



				@bot.message_handler(commands=['start'])
				def send_welcome(message):
				    userid = int(message.from_user.id)
				    usrinfo = bot.get_chat_member(userid, userid).user
				    bot.send_message(message.chat.id, "Hi, " + usrinfo.first_name + "!\nSend me any photo or file and I will save it on your (host) PC\n\nTo view supported files, enter the command\n/files")

				@bot.message_handler(commands=['files'])
				def send_files(message):
				    bot.send_message(message.chat.id, 'The list is not complete. many files have not been checked yet, try to send any and if you see the message "Saved" , then your file is saved\n\nSupported:\nArchives\nPhoto\n.torrent\n.exe\n.py\n.txt\n\nIf your file is not supported, add it to the archive and send it to the bot')

				@bot.message_handler(content_types=['photo', 'document'])
				def handler_file(message):
				    if message.content_type == 'photo':
				        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
				        downloaded_file = bot.download_file(file_info.file_path)
				        src = f'files/' + file_info.file_path.replace('photos/', '')
				        with open(src, 'wb') as new_file:
				            new_file.write(downloaded_file)
				            bot.send_message(message.chat.id, "Saved")
				            print(Style.BRIGHT + Fore.MAGENTA + "Saved "  + Style.RESET_ALL + src)

				    elif message.content_type == 'document':
				        file_info = bot.get_file(message.document.file_id)
				        downloaded_file = bot.download_file(file_info.file_path)
				        src = f'files/' + message.document.file_name
				        with open(src, 'wb') as new_file:
				            new_file.write(downloaded_file)
				            bot.send_message(message.chat.id, "Saved")
				            print(Style.BRIGHT + Fore.MAGENTA + "Saved "  + Style.RESET_ALL + src)
				bot.polling()



			if choose_psb == "2":
				print(Style.BRIGHT + Fore.MAGENTA + """	Token will only be set after restarting Kali Helper
			    Enter new Token""" + Style.RESET_ALL)
				newtoken = input()
				token_file = open("token1.py", "w") 
				token_file.write(f'TOKEN1 = "{newtoken}"')
			if choose_psb == "99":
				m = 2
	if choose == "9":
		os.system("clear")
		print(faded_cbf)
		capfile = input (Fore.YELLOW + "Enter Cap File name (with .cap)\n" + Style.RESET_ALL)
		brutelist = input (Fore.YELLOW + "Enter Brute List neme (with .txt)\n" + Style.RESET_ALL)
		bssid = input (Fore.YELLOW + "Enter BSSID of hacked network\n" + Style.RESET_ALL)
		print(Fore.YELLOW + """				Brute will start in 10 seconds
	exit with "Ctrl + C" or window close won't work and brute force will continue in background mode
			Either wait until the end or restart your computer""" + Style.RESET_ALL)
		sleep(10)
		os.system("aircrack-ng -w " + brutelist + " -b " + bssid + " " + capfile)
		input(Fore.YELLOW + """If password is not found, try another BruteList
	Press enter for continue""" + Fore.WHITE)
	if choose == "99":
		a = 2
