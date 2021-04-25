import aws
import os, docker, lvm, hadoop as hd, linux

os.system("tput setaf 3")


while(True):
    os.system("clear")
    print("\t\t------->Technologies Integration<------")
    os.system("tput setaf 7")
    print("\n")
    print(

"""
\t\t\tPress 0: Exit
\t\t\tPress 1: DOCKER
\t\t\tPress 2: HADOOP
\t\t\tPress 3: AWS
\t\t\tPress 4: LVM
\t\t\tPress 5: LINUX

"""
)
    choice = int(input("Enter The Choice :-> "))

    if choice==0:
         break
    if choice ==1:
        docker.main_menu()
    if choice == 2:
        hd.HadoopStart()
    if choice ==3:
    if choice == 4:
        lvm.main_loop()
    if choice == 5:
        linux.StartLinux()
