import boto3, os

def create_keypair(x):
    ec2 = boto3.resource('ec2')
    outfile = open(x,'w')
    keypair = ec2.create_key_pair(KeyName=x)
    KeyPairOut = str(key_pair.key_material)
    print(KeyPairOut)
    outfile.write(KeyPairOut)
    outfile.close()

    print("Key pair", x, "created successfully and public key saved in this directory.")

def create_sg(x):
    os.system("aws ec2 create-security-group --group-name {} --description my_{}".format(x,x))
    os.system("aws ec2 authorize-security-group-ingress --group-name {} --protocol tcp --port 80 --cidr 0.0.0.0/0")

    print("Security group", x, "created successfully.")

def show_instances():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")


def create_instance(keyname, sg):
    ec2_client = boto3.client("ec2", region_name="ap-south-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0b0154d3d8011b0cd",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName=keyname
    )

    print("Instance", instances["Instances"][0]["InstanceId"], "created successfully.")

def ebs_volume(x):
    os.system("aws ec2 create-volume --availability-zone ap-south-1 --size {}",format(int(x)))

    print("Volume of size", x, "created successfully.")

def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))
