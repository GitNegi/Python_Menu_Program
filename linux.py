import os

os.system("tput setaf 3")
print("\t\t------>LINUX<-------")
os.system("tput setaf 7")
print("\n")

while(True):
    print(
"""

\t\tPress 0: Exit
\t\tPress 1: Present Working Directory
\t\tPress 2: Show Hidden Folder
\t\tPress 3: list File|Folder
\t\tPress 4: print File Data
\t\tPress 5: copy File|Folder
\t\tPress 6: move File|Folder
\t\tPress 7: make Directory|Folder
\t\tPress 8: Create file
"""
)
    x = int(input("Enter Your Choice :-> "))
    if x == 0:
        break

    if x == 1:
        os.system("pwd")

    if x == 2:
        os.system("ls -a {}".format(input("Enter Folder Location :-> ")))

    if x == 3:
        os.system("ls {}".format(input("Enter File|Folder Location :-> ")))

    if x == 4:
        os.system("cat {}".format(input("Enter File Name + Location :-> ")))

    if x == 5:
        os.system("cp {} {}".format(input("Enter File|Folder To Be Copy + Location : "),input(" Destimation Location : ")))

    if x == 6:
        os.system("mv {} {}".format(input(" File|Folder To be Move With Location : "),input(" Destination Location : ")))

    if x == 7:
        os.system("mkdir {}".format(input("Enter Location With Directory Name : ")))

    if x == 8:
        os.system("touch {}".format(input("Enter File name : ")))
