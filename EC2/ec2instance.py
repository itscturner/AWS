import boto3
from botocore.exceptions import NoCredentialsError, ClientError

'''
Create an EC2 Instance
RHEL 9
T2 Medium
US-West-1
'''

def create_ec2_instance():
    try:
        ec2 = boto3.resource('ec2', region_name='us-west-1')
        
        instance = ec2.create_instances(
            ImageId='ami-0f6c1051253397fef',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.medium',
            KeyName='Key-Pair-Name',                    # Key Pair Name
            SecurityGroupIds=['sg-0123456789abcdef0'],  # Security Group ID
            SubnetId='subnet-0abcdef1234567890',        # Subnet ID
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'My-Instance-Name-Tag'}
                    ]
                }
            ]
        )
        print(f"EC2 Instance created with ID: {instance[0].id}")
    except NoCredentialsError:
        print("ERROR: Credentials not available.")
    except ClientError as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    create_ec2_instance()
  
