# -*- coding: utf-8 -*-
import os
import shutil
import pickle
from openpyxl import Workbook

def has_fileDir(dir,global_dir):
    return os.path.exists(global_dir+"/"+dir)

def create_fileDir(dir,global_dir):
    os.makedirs(global_dir+"/"+dir+"/cluster")
    os.makedirs(global_dir+"/"+dir+"/corpus")
    os.makedirs(global_dir+"/"+dir+"/report")
    os.makedirs(global_dir+"/"+dir+"/stopword")
    os.makedirs(global_dir+"/"+dir+"/word2vec")
    return True

def copyTo(src,dst,global_dir):
    shutil.copyfile(global_dir+"/"+src,global_dir+"/"+dst)
    return True

def write_xls(tableValues,report,global_dir):
    tableTitle = ['问题', '答案', '关键词', '同义词','一级目录','二级目录','三级目录','四级目录','五级目录']
    if(has_fileDir(report,global_dir)):
        excelFullName=global_dir+"/"+report+"/template.xls"
        wb = Workbook()
        ws = wb.active
        for col in range(len(tableTitle)):
            c = col + 1
            ws.cell(row=1, column=c).value = tableTitle[col]
        for row in range(len(tableValues)):
            ws.append(tableValues[row])
        wb.save(filename=excelFullName)
        return True
    else:
        return False

def write_pickle(report_dir,global_dir,tableValues):
    pickle.dump(tableValues,open(global_dir+"/"+report_dir+"/pickle.txt","wb"))
    return True

def read_pickle(report_dir,global_dir):
    tableValues=pickle.load(open(global_dir+"/"+report_dir+"/pickle.txt","rb"))
    return tableValues