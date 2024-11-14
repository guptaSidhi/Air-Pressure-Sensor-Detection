import sys
import os 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename 
    linenumber = exc_tb.tb_lineno
    error_message = f"Error occured in [{filename}] at [{linenumber}] with error [{str(error)}]"
    return error_message


class SensorException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)
        
    def __str__(self):
        return self.error_message