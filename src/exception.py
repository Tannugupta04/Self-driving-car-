# for exception handlog purpose
import sys
import logging
# sys libnrary:sys module in python prov9des various function and variables that are used to manipulate different parts of the python runtime enviornment\
def error_message_details(error,error_detail:sys):
# this error detail is present inside the sys
    _,_,exc_tb=error_detail.exc_info()# this willl give 3 info first 2 aam not interetsed in and alst one is given -,-,
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number[{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    return error_message

    

    

    
class CustomException(Exception):# created our own cusum exception class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)#c reated error meggage variable
# inherit the exceotion class here by usingthis

    def __str__(self):
        return self.error_message
    

    # mjust to check
# if __name__=='__main__':
#     try:
#         a=1/0
#     except Exception as e:
#             logging.info("Divide by zero")
#             raise CustomException(e,sys)
        

