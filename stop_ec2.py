import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    # Get all running instances with tag Environment = Learning
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Environment',
                'Values': ['Learning']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )
    
    # Collect instance IDs
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")
    else:
        print("No running instances found with tag Environment=Learning")
    
    return {
        'statusCode': 200,
        'body': f'Stopped: {instance_ids}'
    }