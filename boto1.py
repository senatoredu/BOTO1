import boto3
elb = boto3.client('elbv2')

#Welcome print statement
print (''' This program allows you to progrmatically view the health status of an instance in a target group, all you need are 3 inputs 
           
           TG-ARN: Target Group's ARN
           
           Instance: Instance-id
           
           Listener-Port: Listening-Port of Instance
           
           ''')

#variables input
arn = input("What is the Target-groups' ARN: ")
instance = input("What is the instance-id you would like to check for: ")
listport = input ("What is the instance's listener port: ")

#boto3 elbv2 target health method

response = elb.describe_target_health(
    TargetGroupArn=arn,
    Targets=[
        {
            'Id': instance,
            'Port': listport,
        },
    ],
)

# boto3 elbv2 target health method produces a dictionary response, have no need of metadata key, so extracted only TargetHealthDescriptions
print (response ['TargetHealthDescriptions'])



