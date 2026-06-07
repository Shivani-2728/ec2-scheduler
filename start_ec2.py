import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    # Get all stopped instances with tag Environment = Learning
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Environment',
                'Values': ['Learning']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['stopped']
            }
        ]
    )
    
    # Collect instance IDs
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    if instance_ids:
        ec2.start_instances(InstanceIds=instance_ids)
        print(f"Started instances: {instance_ids}")
    else:
        print("No stopped instances found with tag Environment=Learning")
    
    return {
        'statusCode': 200,
        'body': f'Started: {instance_ids}'
    }