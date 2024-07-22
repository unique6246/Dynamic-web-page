    import json
    import boto3
    from botocore.exceptions import ClientError

    def lambda_handler(event, context):
        # Initialize the DynamoDB client
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('NMIT-Hackathon-table')

        # Extract data from the event
        registration_number = event.get('registrationNumber')
        name = event.get('name')
        branch = event.get('branch')

        # Check if all fields are provided
        if not registration_number or not name or not branch:
            return {
                'statusCode': 400,
                'body': json.dumps('Error: Missing required fields')
            }

        # Prepare the item to be inserted into DynamoDB
        item = {
            'registrationNumber': registration_number,
            'name': name,
            'branch': branch
        }

        # Try to insert the item into the DynamoDB table
        try:
            table.put_item(Item=item)
            return {
                'statusCode': 200,
                'body': json.dumps('Registration successful')
            }
        except ClientError as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error: {e.response["Error"]["Message"]}')
            }

