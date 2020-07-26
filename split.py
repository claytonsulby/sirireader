# -*- coding: utf-8 -*-

import os
import logging
import time
import re

from moveFile import moveFile
from moveFile import getPathLeaf


if __name__ == "__main__":
    
    
    source_path = "/Users/clay/Desktop/split/input/hp5.txt"
    source_filename_split = os.path.splitext(getPathLeaf(source_path))
    dest_path = "/Users/clay/Desktop/split/output/"+source_filename_split[0]+"/"
    
    try:
        os.mkdir(dest_path)
    except:
        pass
    
    file_object  = open(source_path, "r")
    
    
    lines = file_object.readlines()
    
    
    files = 0
    
    # all lines and their types
    if 0:
        
        chapters = []
        headers = []
        pagenumbers = []
        newlines = []
        others = []
        endswith = [] 
        text = []
        
        for i in range(len(lines)):
            
            #line treatment
            if 0:
                lines[i] = lines[i].replace('“','"')
                lines[i] = lines[i].replace('”','"')
                lines[i] = lines[i].replace('‘',"'")
                lines[i] = lines[i].replace('’',"'")
                lines[i] = lines[i].replace('. . .','...')
                lines[i] = lines[i].replace('—','-')

                if lines[i].startswith(' '):
                    lines[i] = lines[i].lstrip()

            #line catrgorization
            if 0:
                if lines[i].startswith('\x0c\x0c'):

                    chapters.append(lines[i])
                    
                elif lines[i].startswith('\x0c'):

                    headers.append(lines[i])
                    
                elif lines[i].startswith('\x91'):
                    
                    pagenumbers.append(lines[i])
                    
                elif lines[i].startswith('\n'):
                    
                    newlines.append(lines[i])
                    
                elif lines[i][0].isalpha() or lines[i][0] == '"':
                    pass
                else:
                    others.append(lines[i])

            #remove elements
            if 0:
                if lines[i].startswith('\x0c\x0c'): #chapters
                    lines[i] = ''
                elif lines[i].startswith('\x0c'): #headers
                    lines[i] = '' 
                elif lines[i].startswith('\x91'): #page numbers
                    lines[i] = ''
                elif lines[i].startswith('\n'): #new lines
                    lines[i] = ''
                elif lines[i][0].isalpha() or lines[i][0] == '"':
                    pass
                else:
                    pass
                                  
            # all lines that end with "-"       
            if 0:
                if len(lines[i]) >= 2 and (lines[i][-3] == "—" or lines[i][-3] == "-"): #yes they're different hiphens, no they don't all look the same
                    endswith.append(lines[i])

    #strip every line in the text
    if 1:
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    
    #remove all lines with no numbers or characters
    if 1:
        
        nochar = []
        for i in range(len(lines)):
            if not any(char.isdigit() for char in lines[i]) and not any(char.isalpha() for char in lines[i]) and lines[i] != '':
                lines[i] = ''

        if [lines[i] for i in range(len(lines)) if not any(char.isdigit() for char in lines[i]) and not any(char.isalpha() for char in lines[i]) and lines[i] != ''] == []:
            logging.info("All lines with no numbers or characters removed")
    
    #remove headers based on first seen chapters
    if 1:
        
        seenchapters = []
        seenheaders = []
        
        for i in range(len(lines)):
            if lines[i] in seenchapters:
                lines[i] = ''
            if lines[i].startswith("CHAPTER") or lines[i].startswith("Chapter"):
                seenchapters.append(lines[i])
                
                j = i
                headerflag = 0
                
                while headerflag == 0:
                    j += 1
                    if lines[j] != '':
                        seenheaders.append(lines[j])
                        headerflag = 1        
                    
        #double check
        chapters = [line for line in lines if line.startswith("CHAPTER") == True]
        if seenchapters == chapters:
            logging.info("All chapters not headers are accounted for")   
            
    #remove hiphenated words on linebreaks and combine lines
    if 1:
        for i in range(len(lines)):
            if lines[i].endswith("-"):
                lines[i] = lines[i][:-1] + lines[i+1]
                i += 1
    
    #remove page numbers
    if 1:

        for i in range(len(lines)):
            if any(char.isdigit() for char in lines[i]) and any(char.isalpha() for char in lines[i]): #any line with number
                pass
            if any(char.isdigit() for char in lines[i]) and not any(char.isalpha() for char in lines[i]): #lines with only numbers
                lines[i] = ''
            if lines[i].endswith('\x91'):
                lines[i] = lines[i][:-16]          
        
        #double check there are no lines with only numbers
        if [lines[i] for i in range(len(lines)) if any(char.isdigit() for char in lines[i]) and not any(char.isalpha() for char in lines[i])] == []:
            logging.info("All page numbers removed")

    #remove nonsingle whitespaces
    if 1:
        for i in range(len(lines)):
            temp = re.search('\s{2,}',lines[i])
            if temp != None:
                lines[i] = re.sub('\s{2,}','',lines[i])

    #join each line
    if 1:
        temp = " ".join(lines)
        
        output = []
        i = 0  
        count = 0
        
        for i in range(len(temp)):
            if count == 3:
                count = 0
                files += 1
                file_object = open(dest_path+"output"+str(files)+".txt", "w")
                output = "".join(output)
                file_object.write(output)
                output = []
            try:    
                if temp[i] == '.' and temp[i+1] != '.':
                    count += 1
            except:
                pass
            output.append(temp[i])
    
            
    #create files by newlines
    if 0:
        
        #init
        output = []
        i = 0  
        linenumber = 0
        
        for line in lines:
            if line == "" and output == []:
            
                lines = lines[1:]

            elif line == "" and output != []:
                
                files += 1
                file_object = open(dest_path+"output"+str(files)+".txt", "w")
                output = " ".join(output)
                file_object.write(output)
                output = []
            else:
                output.append(line)
                lines = lines[1:]
   
    # create files by chapter
    if 0:            
        while lines != []:
            if lines[i] == "":
                
                linenumber+=1
                print(linenumber)
                
                lines = lines[1:]

            elif lines[i].startswith("CHAPTER"):
                
                files += 1
                
                file_object = open("output"+str(files)+".txt", "w")
                output = " ".join(output).replace("\n","")
                file_object.write(output)
                
                output = []
                i = 0  
                
                output.append(lines[i])
                lines = lines[1:]
                
            else:
                
                linenumber+=1
                print(linenumber)
                
                output.append(lines[i])
                lines = lines[1:]
               
    if 0:            
        while lines != []:
            if lines[i] == "":
                
                linenumber+=1
                print(linenumber)
                
                lines = lines[1:]

            elif lines[i].startswith("CHAPTER"):
                
                files += 1
                
                file_object = open("output"+str(files)+".txt", "w")
                output = " ".join(output).replace("\n","")
                file_object.write(output)
                
                output = []
                i = 0  
                
                output.append(lines[i])
                lines = lines[1:]
                
            else:
                
                linenumber+=1
                print(linenumber)
                
                output.append(lines[i])
                lines = lines[1:]
