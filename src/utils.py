# import pandas as pd 
# import numpy as np

# import os 
# import sys
# import json 

# from src.exception import SensorException
# from src.logger import logging
# from src.config import mongo_client

# def dump_csv_mongodb(filepath:str,database_name:str,collection_name:str):
    
#     try:
#         df = pd.read_csv(filepath)
#         df.reset_index(drop=True,inplace=True)
#         json_records = list(json_loads(df.T.to_json()).values())

#         mongo_client[database_name][collection_name].insert_many(json_records)

#     except Exception as e:
#         raise SensorException(e,sys)
    

import pandas as pd
import numpy as np
import os
import sys
import json

from src.exception import SensorException
from src.logger import logging
from src.config import mongo_client

def dump_csv_mongodb(filepath: str, database_name: str, collection_name: str):
    try:
        df = pd.read_csv(filepath)
        df.reset_index(drop=True, inplace=True)
        
        # Convert DataFrame to JSON records
        json_records = json.loads(df.to_json(orient='records'))

        # Insert records into MongoDB
        mongo_client[database_name][collection_name].insert_many(json_records)
        logging.info(f"Successfully inserted records from {filepath} into MongoDB")

    except Exception as e:
        raise SensorException(e, sys)
