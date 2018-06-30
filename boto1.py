import boto3
import sys

try:
    elb = boto3.client('elbv2')
except Exception as e:
    print ("ERROR: failed to connect to EC2")
    sys.exit(1)
     

# Welcome print statement
print(''' This program allows you to progrmatically view the health status of an instance in a target group, all you need are 3 inputs 

           TG-ARN: Target Group's ARN

           Instance: Instance-id

           Listener-Port: Listening-Port of Instance

           ''')

# variables input
arn = input("What is the Target-groups' ARN: ")
instance = input("What is the instance-id you would like to check for: ")
listport = int(input("What is the instance's listener port: "))

# boto3 elbv2 target health method

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

if ((((response ['TargetHealthDescriptions']) [0]) ['TargetHealth']) ['State']) == 'unhealthy':
    print ( "Instance {} is currently {} because: {}".format (instance, ((((response ['TargetHealthDescriptions']) [0]) ['TargetHealth']) ['State']), ((((response ['TargetHealthDescriptions']) [0]) ['TargetHealth']) ['Reason'])))
else:
    print ( "Instance {} is currently {} ".format (instance, ((((response ['TargetHealthDescriptions']) [0]) ['TargetHealth']) ['State'])))


