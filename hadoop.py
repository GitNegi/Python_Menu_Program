import os

os.system("tput setaf 3")
print("\t\t------->HADOOP CLUSTER<-------")
os.system("tput setaf 7")
print("\n")


while(True):
    print(

"""
\t\tPress 0: SERVICE STATUS
\t\tPress 1: SERVICE START
\t\tPress 2: RUNNING CONTAINERS
\t\tPress 3: ALL THE CONTAINERS
\t\tPress 4: START CONTAINER
\t\tPress 5: START CONTAINER WITH TERMINAL
\t\tPress 6: REMOVE CONTAINER WITH FORCE
\t\tPress 7: STOP CONTAINER
\t\tPress 8: LAUNCHED CONTAINER WITHOUT TERMINAL
\t\tPress 9: LAUNCHED WITH TERMINAL
\t\tPress 10: CHECKING DETAILS ABOUT THE CONTAINER
\t\tPress 11: CHECKING LOGS
"""
)
    choice = int(input("Enter The Choice :-> "))

    if choice==0:
         break
    


