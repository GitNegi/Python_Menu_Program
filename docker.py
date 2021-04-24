import os
import subprocess as sp

def chng2num(x,y,z):
        while not(x.isnumeric() and int(x) in range(y,z)):
            x = input("Enter a valid choice \n[docker]$ ")
        else:
            x = int(x)
        return x

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

[docker]$ """)
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

def manage_images():
    while True:
        os.system("clear")
        docker_img = input("""
--------------DOCKER--------------

1. Pull an image
2. Commit image
3. View all images
4. Push an image
5. Go Back

Enter your Choice

----------------------------------

[docker]$ """)
        docker_img = chng2num(docker_img,1,6)
        if docker_img == 1:
            os.system("docker pull {}:{}".format(input("Image Name: "),input("Image Tag: ")))
        elif docker_img == 2:
            os.system("docker commit {}".format(input("Container: ")))
        elif docker_img == 3:
            print(sp.getoutput("docker images"))
            os.system("sleep 2")
        elif docker_img == 4:
            os.system("docker push {}:{}").format(input("Image Name: "),input("Image Tag: ")))
        else:
            break

def main_menu():
        os.system("clear")
        x = input("""
--------------DOCKER--------------

1. Install Docker
2. Start Docker Service
3. Login to Docker
4. Manage Images
5. Manage Containers
6. Go Back

Enter your Choice

----------------------------------

[docker]$ """)
        x = chng2num(x,1,7)
        while True:
            if x == 1:
                os.system("sudo yum install docker -y")
            elif x == 2:
                docker_service()
            elif x == 3:
                os.system("docker login")
            elif x == 4:
                manage_images()
            elif x == 5:
                manage_containers()
            else:
                return

main_menu()
