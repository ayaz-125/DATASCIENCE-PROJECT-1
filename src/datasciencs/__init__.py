import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # this is the format of the loggin 

log_dir = "logs"  # this is the name of the logging folder
log_filepath = os.path.join(log_dir,"logging.log")
# Create the log directory if it doesn't exist
os.makedirs(log_dir,exist_ok=True)   # this is the condition that if the folder is already created or not

logging.basicConfig(  
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datasciencelogger")