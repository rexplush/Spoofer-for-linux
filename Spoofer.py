# !usr/bin/python
import random
import subprocess
import colorama
from colorama import Style, Fore

colorama.init(autoreset=True)
print(Style.BRIGHT + Fore.RED + """
____             ____  _           _     
|  _ \ _____  __ |  _ \| |_   _ ___| |__  
| |_) / _ \ \/ / | |_) | | | | / __| '_ \ 
|  _ <  __/>  <  |  __/| | |_| \__ \ | | |
|_| \_\___/_/\_\ |_|   |_|\__,_|___/_| |_|


""")
print(Fore.GREEN + "Github" ":", Fore.BLUE + " https://github.com/rexplush")
print(Fore.RED + "Instagram" ":", Fore.BLUE + "https://www.instagram.com/rexplush/")
print(Fore.MAGENTA + "©RexPlush")


def macc(interface):
    opt = input("""Hey User dow you want to use:
        [+] Random MAC Address
        [+] Type a MAC Address
        Type 1 or 2 select option respectively:""")
    x = int(opt)
    if x <= 1:
        # this generates random MAC Address
        a = random.randint(10, 20)
        b = random.randint(10, 20)
        c = (a + b)
        e = random.randint(1, 5)
        f = random.randint(5, 9)
        d = str((c + e)) + ':' + str((c + e + f + e)) + ':' + str((c + e + f + f)) + ':' + str(
            (c + e + f + e + f)) + ':' + str((c + e + f + e + e)) + ':' + str((c + e + f + e + e + f + f))
        subprocess.call("ifconfig " + interface + " down", shell=True)
        subprocess.call("ifconfig " + interface + " hw ether %s" % d, shell=True)
        subprocess.call("ifconfig " + interface + " up", shell=True)
        print("Your new MAC Address " + d)

    if x >= 2:
        macaddress = input("""[+]Enter a mac address
            Type a 12 numbers separated using : in between two numbers""")
        subprocess.call("ifconfig" + interface + "down", shell=True)
        subprocess.call("ifconfig" + interface + "hw ether %s" % d, shell=True)
        subprocess.call("ifconfig" + interface + "up", shell=True)
def ipadd(interface):
    import random
    import subprocess
    opt = input("""Hey User dow you want to use:
    [+] Random IP Address
    [+] Type a IP Address
    Type 1 or 2 select option respectively:""")
    if opt <= str(1):
        # this generates random MAC Address
        a = random.randint(10, 20)
        b = random.randint(10, 20)
        c = (a + b)
        e = random.randint(1, 5)
        f = random.randint(5, 9)
        d = str((c + e)) + '.' + str((c + e + f + e)) + '.' + str((c + e + f + f)) + '.' + str((c + e + f + e + f))
        subprocess.call("ifconfig " + interface + " " + d, shell=True)
        print("Your new IP Address " + d)
    if opt >= str(2):
        j = input("""[+]Enter a IP Address
            Type a  numbers separated using : in between two numbers:
            """)
        subprocess.call("ifconfig " + interface + " " + j, shell=True)
        print("Your new IP Address " + j)
interface = input("""Enter a interface name-->""")
opt = input("""Select an option:
    1. Change MAC Address
    2. Change IP Address
    3. Change both
Enter 1, 2, 3 to select an option""")
if opt == str(1) :
    macc(interface)
if opt == str(2) :
    ipadd(interface)
if opt == str(3) :
    macc(interface)
    ipadd(interface)
