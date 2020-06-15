import datetime
import logging
import os

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    test_value = os.environ['TestKey']
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info(
        f'Python timer trigger function ran at {utc_timestamp} and had this value for TestKey: {test_value}')
