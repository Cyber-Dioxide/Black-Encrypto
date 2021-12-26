import os
import json , random
from colorama import Style , Fore


data = json.load(open("data.json"))


ban = """
██████╗ ██╗      █████╗  ██████╗██╗  ██╗                    
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝                    
██████╔╝██║     ███████║██║     █████╔╝                     
██╔══██╗██║     ██╔══██║██║     ██╔═██╗                     
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗                    
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                    
                                                            
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   
                                                            
"""

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)

def banner():
        os.system("clear")

        print(ran,ban)
        print(ran + "\n\t\tV: 2.0.0 'New Release'\t\n")
        print("*" * 63)

        print(Style.BRIGHT+Fore.LIGHTCYAN_EX, "\n" ,"- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Style.BRIGHT+Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Style.BRIGHT+Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        print("\n" , "*" * 63)

banner()

def encrypt():
    text = input(ran + "\nEnter text to encrypt: " + Style.BRIGHT+Fore.LIGHTGREEN_EX)
    enc = ""
    for i in text:
        for j in data.keys():
            if i == j:
                enc = enc + data.get(i)
        if i not in data.keys():
            enc = enc +i
    print(Style.BRIGHT+Fore.LIGHTGREEN_EX + "\n\t\tCopy and send the text: \n\n" + enc)



def decrypt():
    text = input(ran + "\nEnter text to decrypt: " + Style.BRIGHT + Fore.LIGHTGREEN_EX)
    dec = ""
    for i in text:
        for key , value in data.items():
            if i == value:
                dec = dec + key

        if i not in data.values():
            dec = dec +i
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "\n\t\tCopy and send the text: \n\n" + dec)


no = ["no" , "n"]
cont =""
while cont not in no:
    print(ran + "\n\t[1] Encrypt Text\n\t[2] Decrypt Text\n\t[3] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()
    else:
        pass
