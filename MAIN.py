import os, docker

os.system("tput setaf 3")
print("\t\t------->LVM AUTOMATION<------")
os.system("tput setaf 7")
print("\n")


while(True):
    print(

"""
\t\t\tPress 0: Exit
\t\t\tPress 1: DOCKER
\t\t\tPress 2: HADOOP
\t\t\tPress 3: AWS
\t\t\tPress 4: ANSIBLE
\t\t\tPress 5: LVM
\t\t\tPress 6: LINUX

"""
)
    choice = int(input("Enter The Choice :-> "))

    if choice==0:
         break
    if choice==1:
        docker.main_menu()
    
