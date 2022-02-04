###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### IMPORT

import os
import string


###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### CLASS

class File_read_write():

    def __init__(self, pathN, readN, writeN) -> None:
        self.pathName : string
        self.pathName = pathN
        self.fileName_read : string
        self.fileName_read = readN
        self.fileName_write : string
        self.fileName_write = writeN

    #def set_PathtoFile(self, new_path):
    #    self.pathName = new_path

    def readFile(self): 
        f = open( (self.pathName + self.fileName_read) , "r")
        content = f.read()
        print(content)
        f.close()
        return content
    
    def readFile_line(self): #geht nicht
        f = open( (self.pathName + self.fileName_read) , "r")
        while f.readline():
            print(f.readline())
        f.close()

    def writeFile(self, input, paramter):
        '''
        paramter: "a"=append, "w"=overwrite
        '''
        f = open( (self.pathName + self.fileName_write), paramter)
        f.write( input )
        f.close()

###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### TEST

read_write_obj = File_read_write("Test_Data/", "read_test.csv", "write_test.csv")
content = read_write_obj.readFile()
#read_write_obj.readFile_line()
read_write_obj.writeFile(content, "w")