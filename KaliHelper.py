#CODE BY L1B3RTAS 16.07.2022
import fade
import os
from colorama import Fore, Back, Style
import netifaces
import pathlib
from random import randint
import urllib.request
import socket
import threading
from color import *
main = ("""
██╗  ██╗ █████╗ ██╗     ██╗    ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██║ ██╔╝██╔══██╗██║     ██║    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
█████╔╝ ███████║██║     ██║    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██╔═██╗ ██╔══██║██║     ██║    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██╗██║  ██║███████╗██║    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝   
                                               By l1b3rtaS
					MENU
	1. Update and upgrade all apt library (required to use other functions)
	2. Best Tools from GitHub
	3. Popular programs
	4. Download BrootLists Pack    
	5. Local SSH start
	6. Neofetch
	7. 2vol.msg (P2P Chatting)

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
				os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg")
				os.system("sudo apt-get install sublime-text")
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
				os.system("rm discord.deb")
				print (Fore.RED + """
					Discord Download completed

					To add a shortcut, go to the Kali menu (top right), 
					find the desired program in the search, 
					right-click on it and select "Add to desktop"
					for uninstall use command "apt remove <name>"
					"""
					 + Fore.WHITE)
				input(Fore.RED + "Press enter for continue")
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
				        if msg.decode('ascii') == '__join':
				            print(f'SERVER> Client {client_id} joined chat') 
				            continue
				        print('\r\r' + msg.decode('ascii'))
				        msg = f'{msg.decode("ascii")}'
				        for member in members:
				            if member == addr:
				                continue
				            server.sendto(msg.encode('ascii') , member)
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
			""")
				lipu = input()
				def listen(server: socket.socket):
				    while True:
				        msg = server.recv(UPD_MAX_SIZE)
				        print('\r\r' + msg.decode('ascii') + '\n' + f'you: ' , end='')
				def connect(host: str = lipu , port: int = 1337):
				    server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
				    server.connect((host,port))
				    threading.Thread(target=listen, args=(server,), daemon=True).start()
				    server.send('__join'.encode('ascii'))
				    while True:
				        msg1 = input(f'you: ')
				        msg = (nickname +  " " + msg1) 
				        server.send(msg.encode('ascii'))
				if __name__ == '__main__':
				    os.system("clear")
				    print(faded_vm)
				    print(f"""            {nickname + Fore.CYAN} , welcome to chat , 
	your nick and color visible for other members
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
						print(Fore.CYAN + """
	Enter new nickname
""" + Fore.WHITE)
						new_nick1 = input()
						nick_file = open("nick.txt", "w") 
						nick_file.write(str(new_nick1))
					if choose_ncf == "2":
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
						if new_color == "1":
							new_nick_color = "color = Fore.BLACK"
						if new_color == "2":
							new_nick_color = "color = Fore.RED"
						if new_color == "3":
							new_nick_color = "color = Fore.GREEN"
						if new_color == "4":
							new_nick_color = "color = Fore.YELLOW"
						if new_color == "5":
							new_nick_color = "color = Fore.BLUE"
						if new_color == "6":
							new_nick_color = "color = Fore.MAGENTA"
						if new_color == "7":
							new_nick_color = "color = Fore.CYAN"
						if new_color == "8":
							new_nick_color = "color = Fore.WHITE"
						color_file = open("color.py", "w") 
						color_file.write("from colorama import Fore, Back, Style \n" + new_nick_color)				
					if choose_ncf == "99":
						e = 2
			if choose_nct == "99":
				d = 2
	if choose == "99":
		a = 2

