import boto3
import logging

logging.basicConfig(level=logging.INFO)

textract = boto3.client('textract')

response = textract.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': 'textract-demo-priti',
            'Name': 'download (1).jpg'
        }
    }
)

for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])
        logging.info(block['Text'])
