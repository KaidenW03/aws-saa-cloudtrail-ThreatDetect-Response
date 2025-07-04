import json
import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')

def lambda_handler(event, context):
    # Log the full event for debugging
    logger.info("Received event: %s", json.dumps(event))

    try:
        # Extract key information from the CloudTrail event
        user_identity = event['detail']['userIdentity']['type']
        event_name = event['detail']['eventName']
        source_ip = event['detail']['sourceIPAddress']
        time = event['detail']['eventTime']

        message = f"""
        AWS Security Alert

        Suspicious activity detected in your AWS account!

        • Event: {event_name}
        • Identity Type: {user_identity}
        • Source IP: {source_ip}
        • Time: {time}

        Review this activity immediately.
        """

        logger.info("Alert message composed.")

        # Send SNS Alert
        sns = boto3.client('sns')
        sns.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject='[SECURITY ALERT] Root Login Detected'
        )

        logger.info("SNS alert sent successfully.")

        return {
            'statusCode': 200,
            'body': json.dumps('Security alert sent successfully!')
        }

    except Exception as e:
        logger.error("Error processing event: %s", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps('Error in Lambda function')
        }
