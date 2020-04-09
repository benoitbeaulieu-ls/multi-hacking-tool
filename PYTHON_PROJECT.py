import subprocess 
from socket import *
import time
#All menus are going to be stored here

tools= ["1) gobuster",
        "2) hydra",
        "3) john the ripper",
        "4) Burpsuite",
        "5) Port Scanner",

]

hydra_options= ["1) SSH",
                "2) HTTP-GET",
]

yes_or_no= ["1) Yes",
            "2) No",
]


for tool in tools:
    print(tool)


tool_select=int(input("what tool would you like to use?"))

#This is go buster
if tool_select == 1:
    subprocess.run('ping 8.8.8.8' , shell=True)

#This is Hydra
if tool_select == 2:
    for option in hydra_options:
        print(option)

    option_select=int(input("What option would you like to use? "))
    if option_select == 1:
        subprocess.run("ls" , shell=True)


#This is the port scanner
if tool_select == 5:
    if __name__ == '__main__':
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


restart=str(input("Would you like to try another option? "))

for x in yes_or_no:
    print(x)

if restart == "yes":
    print("You selected yes")
    for tool in tools:
        print(tool)

