import subprocess 
from socket import *
import time

if __name__ == '__main__':
#All menus are going to be stored here

    tools= {
            1: "ping",
            2: "hydra",
            3: "GoBuster",
            4: "john the ripper",
            5: "Burpsuite",
            6: "Port Scanner",

        }

    hydra_options= {
            1: "SSH",
            2: "HTTP-GET",

    }
    

    yes_or_no= ["1) Yes",
            "2) No",
    ]


for number, tool in tools.items():
    print(str(number)+" " + tool)

option=int(input("what tool would you like to use?"))



#All Fuctions will go here

# ping a host function
def ping():
    host = str(input("what host would you like to ping?"))
    subprocess.run('ping %s' %(host) , shell=True)

# Hydra Bruteforce Function
def hydra():
    for number, optionselect in hydra_options.items():
        print(str(number)+ " " + optionselect)
    option= int(input("What are you trying to bruteforce? "))

    if option == 1:
        print("SSH Selected")
        user= str(input("what user are you tryng to bruteforce? "))
        wordlist= str(input("specify your wordlist path "))
        targetIP= str(input("What is the target IP "))
        subprocess.run('hydra -l %s -P '  %(user) + wordlist + ' ' + targetIP +' ssh -t 4' , shell=True)

# GoBuster Directoy Bruteforce Function 
def gobuster():
    pass

# John The Ripper Bruteforce Function
def john():
    pass

# Burpsuite Open Function
def burp():
    pass

# Stealth Port Scanner Function
def portscanner():
    target = input('Enter the host to be scanned: ')
    first_Port = int(input("What port would you like to start with? "))
    last_Port = int(input("What is the ending port?"))
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)

    for i in range(first_Port, last_Port):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))

        if(conn == 0):
            print ('Port %d: OPEN' % (i,))

        s.close()

    print("Scan finished")



if option == 1:
    ping()

if option == 2:
    hydra()

if option == 3:
    gobuster()

if option == 4:
    john()

if option == 5:
    burp()

if option == 6:
    portscanner()
 
