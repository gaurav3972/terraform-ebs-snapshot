import boto3
import datetime
import os

# Create EC2 and SNS clients
ec2 = boto3.client('ec2')
sns = boto3.client('sns')

def lambda_handler(event, context):
    # Get today’s date in YYYY-MM-DD format
    today = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    
    # Filter for EBS volumes with tag Snapshot=true
    volumes = ec2.describe_volumes(
        Filters=[{'Name': 'tag:Snapshot', 'Values': ['true']}]
    )

    snapshots = []

    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        description = f"Snapshot of {volume_id} taken on {today}"
        
        # Create snapshot with tags
        snapshot = ec2.create_snapshot(
            VolumeId=volume_id,
            Description=description,
            TagSpecifications=[{
                'ResourceType': 'snapshot',
                'Tags': [{'Key': 'CreatedOn', 'Value': today}]
            }]
        )

        snapshots.append(snapshot['SnapshotId'])
        print(f"Snapshot created: {snapshot['SnapshotId']}")

    # If snapshots were created, send notification
    if snapshots:
        sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Subject='EBS Snapshot Backup Complete',
            Message=f"Created snapshots: {', '.join(snapshots)}"
        )
        
    return {
        'statusCode': 200,
        'body': f"Snapshots created: {snapshots}"
    }