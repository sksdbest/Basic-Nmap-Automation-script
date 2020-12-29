import os
import subprocess

def mainMenu():
    print("*************************** Automated Network Scanner **************************\n")
    print("************************************  Menu  ************************************\n")
    print("\t\t\t 1. Check My IP Address")
    print("\t\t\t 2. Basic Nmap Scan")
    print("\t\t\t 3. Update Nmap Script-DataBase")
    print("\t\t\t 4. Port Discovery")
    print("\t\t\t 5. Nmap All Scripts at Once")
    print("\t\t\t 6. XMAS Scan")
    print("\t\t\t 99. Quit The Program")
    print()
    choice = int(input("Select Your Option : "))
    if choice == 1:
        check_ip()
        mainMenu()
    elif choice == 2:
        bnmap()
        mainMenu()
    elif choice == 3:
        update_nmap()
        mainMenu()
    elif choice == 4:
        port_discovery()
        mainMenu()
    elif choice == 5:
         nmap_all()
         mainMenu()
    elif choice == 6:
         nmap_xmas()
         mainMenu()
    elif choice == 99:
        clear()
        quit_Program()
    else:
        print("Invalid Choice :")
        mainMenu()




def check_ip():
    my_ip=subprocess.check_output(['bash','-c','ifconfig eth0 | grep "inet " '])  
    print("This is your IP Address  :", my_ip)
   


def update_nmap():
    print('-' * 80)
    subprocess.check_call(
        ['sudo','nmap', '--script-updatedb'])
    print('-' * 80)


 
def bnmap():
    host=input("[*]Please Enter Host Address To Scan : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap','-T4','-v', host])
    print('-' * 80)


def port_discovery():
    port = input("[*]Please Enter Host Address To Scan : ")
    subprocess.check_call(
        ['nmap', '-T4','-v','-p 1-6635', port])
        
        
def nmap_all():
    port = input("[*]Please Enter Host Address To Scan : ")
    subprocess.check_call(
        ['sudo','nmap', '-T4','--script', 'all', port])
   
        
def nmap_xmas():
    port = input("[*]Please Enter Host Address To Scan : ")
    subprocess.check_call(
        ['sudo','nmap', '-T4','-sX', port])


def Host_DisCov():
    host=input("[*]Please Enter Host Address To Scan : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n','-v', '-Pn', '-sn','-sL','-PE', '-PP','-oN','hostlist.txt', host])
    print('-' * 80)



def os_discovery():
    os = input("[*]Please Enter Host Address To Scan : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n','-F','-A','-v', '-Pn','-sS','-O','-oN','os_Discove.txt', os])
    print('-' * 80)



def port_discoveryInRange():
    port = input("[*]Please Enter Host Address To Scan : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap','-p','1-100','-oN','Port_DiscoverInRange.txt', port])
    print('-' * 80)
 


def clear():
    os.system('cls||clear')




def quit_Program():
    quit()




if __name__ == '__main__':
    mainMenu()
