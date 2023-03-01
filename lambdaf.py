from json import dumps

def lambda_handler(event, context):
    # TODO implement
    print('holaaaaa')
    return {
        'statusCode': 200,
        'body': dumps('Hello from Lambda!')
    }