import json
import logging
import urllib.parse
LOG = logging.getLogger(__name__)

def hello(event, context):
    LOG.warning('Event :%s',event)
    if 'Records' in event:
        for record in event['Records']:
            try:
                LOG.info('Processing record %s', record)
                bucket = record['s3']['bucket']['name']
                key = urllib.parse.unquote_plus(record['s3']['object']['key'])
                LOG.info('New s3 file recieved - %s', key)
            except Exception as exception:  # pylint:disable=broad-except
                LOG.error(exception)
                LOG.error('Caught error: ', exc_info=True)
    else:
        LOG.warning('No records in payload')

    body = {
        "message": "Hello---",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


