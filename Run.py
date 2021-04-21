import string
from random import *
import time
import os
try:
    from colorama import Fore
except:
    print(Fore.RED+"Please install colorama module")
    time.sleep(3)
while True:
    time.sleep(0.1)
    os.system("cls")
    print(Fore.BLUE+"<<<",Fore.MAGENTA+"Password"+Fore.WHITE+"-"+Fore.RED+"Maker",Fore.BLUE+">>>\n")
    time.sleep(0.1)
    print(Fore.YELLOW+"You can type",Fore.RED+"( 0 )",Fore.YELLOW+"to exit app\n")
    time.sleep(0.1)
    try:
        get_char = int(input(Fore.CYAN+"Please enter your characters number : "))
        if get_char == 0:
            time.sleep(0.1)
            print(Fore.RED+"\nExiting ... ")
            time.sleep(2)
            os.system("cls")
            break
        else:
            getnum = int(input(Fore.GREEN+"\nPlease enter the number of passwords you want to create : "))
            char = string.hexdigits + string.digits
            f = open("password.txt","w+")
            for i in range(getnum):
                password = "".join(choice(char) for q in range(randint(get_char,get_char)))
                print(Fore.GREEN+"\nyour password :",Fore.WHITE+f"{password}")
                f.write(f"{password}\n")
            
            f.close()    
            print(Fore.CYAN+"\n\nyour password character is : "+Fore.WHITE+f"{get_char}\n")
            print(Fore.CYAN+"your password number is : "+Fore.WHITE+f"{getnum}\n")
            input(Fore.RED+"Perss enter ... ")
            print("")
    except:
        print(Fore.RED+"\nPlease enter a number and nothing else ...")
        time.sleep(3)
