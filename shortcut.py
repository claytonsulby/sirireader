def getfile(fname):
    #gets file
    
    
    return fname

def safefile(fname, contents):
    #saves contents to file with fname
    return 0

def deletefile(fname):
    #deletes file at fname
    return 0

def choosefrommenu(choice):
    menu = {
        "Yes":True,
        "Start from the beginning":False
    }
    return menu.get(choice)

def speaktext(text):
    print(text)
    return

def siriread(number):
    #reads and recursively loops through folders of textfiles starting at the specified number
    
    init = getfile("init.txt")
    
    if not init: #if init doesn't have any value
        
        initcontents = "init"
        savefile(init, initcontents)
        
        info = getfile("info.txt")
        
        if info: #if info.txt has any vaule
            if choosefrommenu("Yes"):
                siriread(info) #stored value for info
            else:
                deletefile(info) #reset value of info
                siriread(info)
        else:
            safefile(info, 1)
            siriread(info)
    else:
        info = getfile("info.txt")
        savefile(info, number)
        count = number
        script = getfile("output"+number+".txt")
        speaktext(script)
        count += 1
        siriread(count)



if __name__ == "__main__":

            
        