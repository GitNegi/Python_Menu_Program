import os
import ec2
import subprocess as sp

def chng2num(x,y,z):
        while not(x.isnumeric() and int(x) in range(y,z)):
            x = input("Enter a valid choice \n[aws]$ ")
        else:
            x = int(x)
        return x

def aws_ec2():
    while True:
        os.system("clear")
        aws = input("""
-------Amazon Web Services--------

1. Create a key pair
2. Create security group
3. Provision the instance
4. Show running instances
5. Stop instance
6. Terminate instance
7. Get public IP
8. Create a volume
9. Attach volume
10. Go Back

Enter your Choice

----------------------------------

[aws]$ """)
        aws = chng2num(aws,1,11)
        if aws == 1:
            ec2.create_keypair(input("Enter the name of the key: "))
        elif aws == 2:
            ec2.create_sg(input("Enter the name of the security group: "))
        elif aws == 3:
            ec2.create_instance(input("Enter name of key: "), input("Enter name of security group: "))
        elif aws == 4:
            ec2.show_instances()
        elif aws == 5:
            ec2.stop_instance(input("Enter the instance ID: "))
        elif aws == 6:
            ec2.terminate_instance(input("Enter the instance ID: "))
        elif aws == 7:
            ec2.get_public_ip(input("Enter the instance ID: "))
        elif aws == 8:
            ec2.ebs_volume(input("Enter the size in GB: "))
        elif aws == 8:
            ec2.ebs_volume(input("Volume ID: "), input("Instance ID: "), input("Device: /dev/"))
        else:
            break

def aws_s3():
    while True:
        os.system("clear")
        aws_svc = input("""
-------Amazon Web Services--------

1. Upload file to bucket
2. Go Back

Enter your Choice

----------------------------------

[aws]$ """)
        aws_svc = chng2num(aws_svc,1,4)
        if aws_svc == 1:
            s3.upload_s3(input("Path to file: "), input("File name after uploading: "))
        else:
            return


def aws_configure():
    while True:
        os.system("clear")
        aws_svc = input("""
-------Amazon Web Services--------

1. Install aws-cli
2. Configure AWS
3. Go Back

Enter your Choice

----------------------------------

[aws]$ """)
        aws_svc = chng2num(aws_svc,1,4)
        if aws_svc == 1:
            os.system("pip3 install awscli boto3")
        elif aws_svc == 2:
            os.system("aws configure")
        else:
            return

def main_menu():
    while True:
        os.system("clear")
        x = input("""
-------Amazon Web Services--------

1. Configure AWS
2. Manage ec2 services
3. Upload to s3
4. Go Back

Enter your Choice

----------------------------------

[aws]$ """)
        x = chng2num(x,1,5)
        if x == 1:
            aws_configure()
        elif x == 2:
            aws_ec2()
        elif x == 3:
            aws_s3()
        else:
            return

main_menu()
