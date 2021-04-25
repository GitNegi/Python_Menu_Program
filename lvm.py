import os

os.system("tput setaf 3")
print("\t\t------>LVM AUTOMATION<-------")
os.system("tput setaf 7")
print("\n")

while(True):
    print(
"""

\t\tPress 0: Exit
\t\tPress 1: To HardDisks Details
\t\tPress 2: Create Physical Volume
\t\tPress 3: Display Physical Volume
\t\tPress 4: Create Volume Group
\t\tPress 5: Display Volume Group
\t\tPress 6: Create Partition of Volume Group
\t\tPress 7: Format the Partition
\t\tPress 8: Mount the Formatted Partition
\t\tPress 9: Extend the Volume
\t\tPress 10: Decrease the Volume
\t\tPress 11: See

"""
)
    x = int(input("Enter Your Choice :-> "))
    if x == 0:
        break
