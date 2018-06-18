import boto3
elb = boto3.client('elbv2')

print (''' This program allows you to progrmatically view the health status of an instance in a target group, all you need are 3 inputs 
           
           TG-ARN: Target Group's ARN
           
           Instance: Instance-id
           
           Listener-Port: Listening-Port of Instance
           
           ''')

arn = input("What is the Target-groups' ARN: ")
instance = input("What is the instance-id you would like to check for: ")
listport = input ("What is the instance's listener port: ")


response = elb.describe_target_health(
    TargetGroupArn=arn,
    Targets=[
        {
            'Id': instance,
            'Port': 80,
        },
    ],
)

print (response ['TargetHealthDescriptions'])



