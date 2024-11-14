from src.exception import SensorException
from src.logger import logging
import os
import sys

def test_exception():
    try:
        a = 1/0
    except Exception as e:
        raise SensorException(e,sys)
    
if __name__ == '__main__':
    try:
        logging.info('Calling the Function')
        test_exception()
    except Exception as e:
        print(e)