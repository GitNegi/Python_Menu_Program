import os

os.system("tput setaf 3")
print("\t\t------->DOCKER<------")
os.system("tput setaf 7")
print("\n")


while(True):
    print(

"""
\t\tPress 0: EXIT
\t\tPress 1: SERVICE STATUS
\t\tPress 2: SERVICE START
\t\tPress 3: RUNNING CONTAINERS
\t\tPress 4: ALL THE CONTAINERS
\t\tPress 5: START CONTAINER
\t\tPress 6: START CONTAINER WITH TERMINAL
\t\tPress 7: REMOVE CONTAINER WITH FORCE
\t\tPress 8: STOP CONTAINER
\t\tPress 9: LAUNCHED CONTAINER WITHOUT TERMINAL
\t\tPress 10: LAUNCHED WITH TERMINAL
\t\tPress 11: CHECKING DETAILS ABOUT THE CONTAINER
\t\tPress 12: CHECKING LOGS
"""
)
    choice = int(input("Enter The Choice :-> "))

    if choice == 0:
         break

    if choice == 1:
        os.system("systemctl status docker")
    

    if choice == 2:
        os.system("systemctl start docker")
    
    if choice == 3:
        os.system("docker ps")

    if choice == 4:
        os.system("docker ps -a")

    if choice == 5:
        x = input("enter the container id")
        os.system("docker start {contName}".format(contName=x))
