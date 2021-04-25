import os

def lvm_pause():
    wait = input("press <Return> to continue")

def main_menu():
    main_menu = input("""
----------LVM Automation----------

1. Physical Volumes
2. Volume Groups
3. Logical Volumes
4. Exit

----------------------------------

Type the desired number:""")
    return main_menu

def lvm_pv():
    while True:
        os.system("clear")
        x = input("""
---------Physical Volumes---------

1. Create a Physical Volume
2. Show all Physical Volumes
3. Show all disks
4. Show a specific disk
5. Go back

----------------------------------

Type the desired number:""")
        if x == "1":
            os.system("pvcreate /dev/{}".format(input("\nEnter name of the disk: ")))
            lvm_pause()
        elif x == "2":
            os.system("pvdisplay")
            lvm_pause()
        elif x == "3":
            os.system("fdisk -l")
            lvm_pause()
        elif x == "4":
            os.system("fdisk -l /dev/{}".format(input("\nEnter name of the disk: ")))
            lvm_pause()
        elif x == "5":
            break
        else:
            print("Enter a valid number")
            lvm_pause()

def lvm_vg():
    while True:
        os.system("clear")
        x = input("""
----------Volume Groupss----------

1. Create a volume group
2. Show all volume groups
3. Show a volume group
4. Add a physical volume
5. Go back

----------------------------------

Type the desired number:""")
        if x == "1":
            os.system("vgcreate {} {}".format(input("\nEnter the name of volume group: "), input("\nEnter the location of all the physical volumes: ")))
            lvm_pause()
        elif x == "2":
            os.system("vgdisplay")
            lvm_pause()
        elif x == "3":
            os.system("vgdisplay {}".format(input("\nEnter the name of volume group: ")))
        elif x == "4":
            os.system("vgextend {} {}".format(input("\nEnter the name of volume group: "), input("\nEnter the location of all the physical volumes: ")))
            lvm_pause()
        elif x == "5":
            main_loop()
        else:
            print("Enter a valid number")
            lvm_pause()

def lvm_lv():
    while True:
        os.system("clear")
        x = input("""
---------Logical Volumess---------

1. Create a Logical Volume
2. Show all Logical Volumes
3. Increase size of lvm
4. Decrease size of lvm
5. Format a logical volume
6. Check filesystem for errors
7. Resize a filesystem
8. Go back

----------------------------------

Type the desired number:""")
        if x == "1":
            os.system("lvcreate --size {}G --name {} {}".format(input("\nEnter the size in GB: "), input("\nEnter the name of the logical volume: "), input("\nEnter the name of the volume group: ")))
            lvm_pause()
        elif x == "2":
            os.system("lvdisplay")
            lvm_pause()
        elif x == "3":
            os.system("lvextend --size +{}G {}".format(input("\nEnter the size in GB: "), input("\nEnter the location of lv: ")))
            lvm_pause()
        elif x == "4":
            os.system("lvreduce -L {}G {}".format(input("\nEnter the size in GB: "), input("\nEnter the location of lv: ")))
            lvm_pause()
        elif x == "5":
            os.system("mkfs.ext4 {}".format("\nEnter the location of lvm: "))
        elif x == "6":
            os.system("e2fsck -f {}".format("\nEnter the location of lvm: "))
        elif x == "7":
            os.system("resize2fs {}".format("\nEnter the location of lvm: "))
        elif x == "8":
            main_loop()
        else:
            print("Enter a valid number")
            lvm_pause()

def main_loop():
    while True:
        os.system("clear")
        x = main_menu()
        if x == "1":
            lvm_pv()
        elif x == "2":
            lvm_vg()
        elif x == "3":
            lvm_lv()
        elif x == "4":
            break
        else:
            print("Enter a valid number")
            lvm_pause()
