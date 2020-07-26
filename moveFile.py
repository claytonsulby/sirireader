import os
import shutil
import ntpath
import logging
import time

from time import time
from os import path

def getSource():
    source = '/Users/clay/Desktop/Input/'
    return source

def getDest():
    dest = '/Users/clay/Desktop/Output/'
    return dest

def watchForFile():
    logging.info('Beginning watchForFile')
    return -1

def getPathLeaf(path):
    logging.info('Beginning getFolder')  
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def getFileNames(path):
    logging.info('Beginning getFileName')
    return os.listdir(path)

def moveFile(filename, source, dest):
    
    logging.info('Beginning moveFile')
    
    
    #ignore .DS_Store
    if filename.startswith('.'):
        return
        
    #if path exists
    if path.exists(dest+filename):
        
        try:    
            os.mkdir(dest + 'Backup/')
        except OSError:
            pass
                
        #if file exists
        if path.isfile(dest+filename):

            #appends whole number time to file
            filename = os.path.splitext(filename)
            var_time = str(time()).split('.')[0]
            timed_filename=filename[0]+' ['+var_time+']'+filename[1]
            filename = filename[0] + filename[1]
        
        #if folder exists
        if path.isdir(dest+filename):
            
            var_time = str(time()).split('.')[0]
            timed_filename=filename+' ['+var_time+']'

            os.rename(dest + filename, dest + 'Backup/' + timed_filename)
            
    os.rename(source + filename, dest + filename)
    
    return 0


if __name__ == "__main__":
    source = getSource()
    dest = getDest()
    
    for item in getFileNames(source):
        moveFile(item, source, dest)