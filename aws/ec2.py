import boto3

def create_keypair(x):
    ec2 = boto3.resource('ec2')
    outfile = open(x,'w')
    keypair = ec2.create_key_pair(KeyName=x)
    KeyPairOut = str(key_pair.key_material)
    print(KeyPairOut)
    outfile.write(KeyPairOut)
    outfile.close()

def create_sg(x):
    pass

def create_instance():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0b0154d3d8011b0cd",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2-key-pair"
    )

    print("Instance", instances["Instances"][0]["InstanceId"], "created successfully.")
