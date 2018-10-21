import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import sys
import os

from swmm_tools import *
from _consts import *
from wadi_tools import *
from cfg import *
import cfg
from da_utils import *

def replace_original_rain():
    # if we skip the forward update, we have to use the original list
    output_list = get_outputs()
    for src_file, dest_file in zip(output_list, originals):
        shutil.copy(src_file, cfg.gdir_name+slash+dest_file)
        debuglog ('Copying file {} to {} folder as {}'.format(src_file, cfg.gdir_name, dest_file))
        shutil.copy(src_file, model_dir+slash+dest_file)
        debuglog ('Copying file {} as {}'.format(src_file, model_dir+slash+dest_file))
        #pause()

def update_best_matrix():
    cfg.best_matrix = cfg.factor_matrix

def feasible(individual):
    for v in individual:
        if not inf_lim < v < sup_lim:
            return False
    return True

def distance(individual):
    error_count = 0
    for v in individual:
        if not inf_lim < v < sup_lim:
            error_count += 1
    return error_count

def loadRainfall(filename, changeDir = True):
    if changeDir:
        data =  np.loadtxt('{}{}{}'.format(model_dir,slash,filename), dtype = str, delimiter =  '\t')
    else:
        data = np.loadtxt(filename, dtype = str, delimiter = '\t')
    return data

def isNow(data):
    if data[yearc] != cfg.gyear or data[monthc] != cfg.gmonth or data[dayc] != cfg.gday or data[hourc] != cfg.ghour or data[minc] != cfg.gminute:
        return False
    return True

def getNowLine(data):
    for i, r in enumerate(data):
        if isNow(r):
            startLine = i - ndata + 1
            if startLine < 0:
                startLine = 0
            break
    return startLine

def getSimulatedLevel(node):
    print(spreadsheet)
    model = SwmmTools(swmm_file, spreadsheet)
    model.run_swmm()
    return model.get_level_by_id(node)

#def getStartDateTime():
    #model = SwmmTools(swmm_file, spreadsheet)


#def getNPeriods():
    #model = SwmmTools(swmm_file, spreadsheet)
    #return model.get_Nperiods()

#def getSimulationTimeStep():
    #model = SwmmTools(swmm_file, spreadsheet)
    #return model.get_report_step()

def deviation(t):
    niveis = getSimulatedLevel(info_node)
    nivel_sim = niveis[t]
    erro = (cfg.gnivel_obs - nivel_sim)**2
    if erro < cfg.minor_error:
        cfg.minor_error = erro
    return erro

def save_best_k(k_array):
    debuglog('Saving best k vector')
    np.savetxt('k_array.txt', k_array, delimiter = '\t', fmt='%s')

def save_k_matrix():
    debuglog('Saving best k_matrix')
    np.savetxt('matrix_k.txt', cfg.best_matrix, fmt = '%s')
    src = 'matrix_k.txt'
    dest = 'matrix.txt'
    shutil.copy(src, cfg.gdir_name+slash+dest)
    debuglog ('Copying file {} to {} folder as {}'.format(src, cfg.gdir_name, dest))

# this function change the rainfall backwards from -k until the current time
def changeRainfall(k_array):
    cfg.factor_matrix = np.array([])
    for original, output, k in zip(originals, outputs, k_array):
        data = loadRainfall(original)
        startLine = getNowLine(data)
        n = ndata - 1
        factor_array = np.array([])
        for i, r in enumerate(data):
            if startLine <= i < startLine + ndata:
                factory = ((-k + 1)/ndata) * n + k
                factor_array = np.append(factor_array, factory)
                n = n - 1
                data[i][rainc] =  float(r[rainc]) * factory
        debuglog('Saving rainfall file {}'.format(output))
        np.savetxt(output, data, delimiter = '\t', fmt = '%s\t%s\t%s\t%s\t%s\t%s\t%.5s')
        cfg.factor_matrix = np.append(cfg.factor_matrix, factor_array)
    cfg.factor_matrix = np.reshape(cfg.factor_matrix, (-1, ndata))
    error = deviation(cfg.gpoi_line)
    penality = distance(k_array)
    mse = error + penality

    if mse < tolerance :
        save_best_k(k_array)
        update_best_matrix()
        save_k_matrix()
        cfg.global_k = k_array
        raise ValueError('done')
    return mse,

def changeRainfallForwards(k_array):
    cfg.factor_matrix = np.array([])
    for output, output_forward, k in zip(outputs, outputs_forward, k_array):
        data = loadRainfall (output, False)
        startLine = getNowLine(data)
        n = ndata - 1
        factor_array = np.array([])
        for i, r in enumerate(data):
            if startLine + ndata <= i < startLine + ndata + ndata:
                factory = ((k - 1)/ndata) * n + 1
                factor_array = np.append(factor_array, factory)
                n = n - 1
                data[i][rainc] =  float(r[rainc]) * factory
        debuglog('Saving rainfall file {}'.format(output_forward))
        np.savetxt(output_forward, data, delimiter = '\t', fmt = '%s')
        cfg.factor_matrix = np.append(cfg.factor_matrix, factor_array)
    cfg.factor_matrix = np.reshape(cfg.factor_matrix, (-1, ndata))

def changeRainfallBypass(k_array):
    try:
        mse = changeRainfall(k_array)[0]
        print('FO: ',mse)
        if mse < cfg.last_mse:
            cfg.last_mse = mse
            cfg.global_k = k_array
            update_best_matrix()
    except:
        raise ValueError('done')
    elapsed_time = get_elapsed_time(cfg.start_time)
    if elapsed_time > time_limit:
        print('Time exceeded. Finishing the optimisation...')
        save_best_k(cfg.global_k)
        save_k_matrix()
        raise ValueError('done')
    return mse
