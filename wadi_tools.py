import os
import sys
import shutil
import logging

# log filename
logfile = 'wadi.log'

# True means the log file will be deleted every time the script starts to run
clearlog = True

# delete the log file, if necessary
if clearlog and os.path.isfile(logfile):
    os.remove(logfile)

logging.basicConfig(filename=logfile, level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p:')

# log text message to the logfile
def debuglog(text):
    logging.debug(text)

def errorlog(text):
    logging.error(text)

# print python version
def which_python():
    print(sys.version)

# pause the execution
def pause():
    _pause = input('Press the [ENTER] key to continue...')

def copy_file(src_file, to):
    shutil.copy(src_file, to)
