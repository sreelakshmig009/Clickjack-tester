from urllib.request import urlopen
from sys import argv, exit
import threading
from colorama import Fore

def check(url):

    try:
        if "http" not in url: url = "http://" + url

        data = urlopen(url,timeout=3)
        headers = data.info()

        if not "X-Frame-Options" in headers: return True
        if not "Content-Security-Policy" in headers: return True

    except: return False


def listVulnerableSite(url):
    f=open("Vulnerable.txt", "a+")
    f.write(url+"\n")
    f.close()

def main():
    try: sites = open(argv[1], 'r').readlines()
    except: print("[*] Usage: python3 clickjack.py <file_name>"); exit(0)

    for site in sites[0:]:
        status = check(site)

        if status:
            print(Fore.RED+"[+] "+Fore.GREEN+site.split('\n')[0] +Fore.WHITE+ " is "+Fore.RED+"Vulnerable")
            listVulnerableSite(site.split('\n')[0])
        
        elif not status: print(Fore.CYAN+"[-] "+Fore.GREEN+site.split('\n')[0] +Fore.WHITE+ " is "+Fore.CYAN+" NOT Vulnerable")
        else: print(Fore.CYAN+'Site crashed, you just got clickjacked')
 
if __name__ == '__main__': 
    main()
