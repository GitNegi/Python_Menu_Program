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
