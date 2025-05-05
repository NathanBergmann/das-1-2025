import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.create_table(
        TableName='cliente',
        KeySchema=[
            {
                'AttributeName': 'cpf',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'cpf',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(resposta)
except Exception as e:
    print(e)