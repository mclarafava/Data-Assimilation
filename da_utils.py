import os
from os.path import join
import cfg
import datetime
import glob, shutil
from cfg import *
from wadi_tools import *

swmm_file = join(model_dir, swmm_filename)
spreadsheet = join(model_dir, spreadsheet_name)

def copy_inp_to_folder (folder):
    copy_file(join(model_dir, swmm_filename), folder)

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def get_dir_name(dt):
    return '{}_{}_{}_{}_{}'.format(dt['year'], dt['month'], dt['day'], dt['hour'], dt['minute'])

# return the name of all created folders
def get_dir_names(raindata):
    folders = []
    dtlist = []
    for dt in raindata:
        folders.append(get_dir_name(dt))
        dtlist.append(dt)
    return folders, dtlist

# copying original rainfall files to the model dir
def copy_input_files():
    input_files = join(input_dir,'*.DAT')
    for file in glob.glob(input_files):
        shutil.copy(file, model_dir)

def get_outputs():
    if skip_forward:
        return outputs
    else:
        return outputs_forward

def set_current_values(dt):
    cfg.gyear = dt['year']
    cfg.gmonth = dt['month']
    cfg.gday = dt['day']
    cfg.ghour = dt['hour']
    print('Hour: {}'.format(cfg.ghour))
    debuglog('Hour: {}'.format(cfg.ghour))
    cfg.gminute = dt['minute']
    cfg.gnivel_obs = dt['nivel_obs']
    cfg.gpoi_line = dt['poi_line']

def get_elapsed_time (start_time):
    now_time = datetime.datetime.now()
    elapsed_time = now_time - cfg.start_step_time
    return elapsed_time.total_seconds()

def process_folder(dt):
    set_current_values(dt)
    cfg.gdir_name = get_dir_name(dt)
    create_dir(cfg.gdir_name)
    copy_inp_to_folder(cfg.gdir_name)
