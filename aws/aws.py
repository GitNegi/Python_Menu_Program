import os
import boto3
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

1. Start Docker Service
2. Stop Docker Service
3. Restart Docker Service
4. Show Service Status
5. Go Back

Enter your Choice

----------------------------------

[aws]$ """)
        aws = chng2num(aws,1,6)
        if aws == 1:
            os.system("systemctl start docker")
        elif aws == 2:
            os.system("systemctl stop docker")
        elif aws == 3:
            os.system("systemctl restart docker")
        elif aws == 4:
            print(sp.getoutput("systemctl status docker | grep Active"))
            os.system("sleep 2")
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
        elif aws_svc == 3:
            break
    return

def docker_service():
    while True:
        os.system("clear")
        docker_svc = input("""
--------------DOCKER--------------

1. Start Docker Service
2. Stop Docker Service
3. Restart Docker Service
4. Show Service Status
5. Go Back

Enter your Choice

----------------------------------

[aws]$ """)
        docker_svc = chng2num(docker_svc,1,6)
        if docker_svc == 1:
            os.system("systemctl start docker")
        elif docker_svc == 2:
            os.system("systemctl stop docker")
        elif docker_svc == 3:
            os.system("systemctl restart docker")
        elif docker_svc == 4:
            print(sp.getoutput("systemctl status docker | grep Active"))
            os.system("sleep 2")
        else:
            return

def docker_login():
    pass

def main_menu():
        os.system("clear")
        x = input("""
-------Amazon Web Services--------

1. Configure AWS
2. Manage ec2 services
3. Login to Docker
4. Manage Images
5. Manage Containers
6. Go Back

Enter your Choice

----------------------------------

[aws]$ """)
        x = chng2num(x,1,7)
        while True:
            if x == 1:
                aws_configure()
            elif x == 2:
                aws_ec2()
            elif x == 3:
                docker_login()
            elif x == 4:
                sp.getoutput("systemctl restart docker")
            elif x == 5:
                sp.getoutput("systemctl restart docker")
            else:
                return

main_menu()
