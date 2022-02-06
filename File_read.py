###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### IMPORT

import os
import string

from File_super import File_super

from String_manipulation import String_manipulation

###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### CLASS

class File_read(File_super):

    '''
    def __init__(self, pathN, fileN) -> None:
        super().__init__(pathN, fileN)
    '''


    def readFile(self) -> None: 
        f = open( self.getPathFileName() , "r")
        self.setFileContent( f.read() )
        f.close()

    
    #
    # Wie kann ich hier eine Methode übergeben? 
    # macht das überhaupt Sinn wenn man es zweil für Zeile macht? 
    #
    def readFile_line(self) -> None: 
        f = open( self.getPathFileName() , "r")
        for line in f:
            str_man = String_manipulation(line)
            #
            str_man.kommaToDot_betweenNumbers()
            #
            line = str_man.getManipulatedString()
            self.addFileContent(line)
        f.close()



###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### TEST

read_obj = File_read("Test_Data/", "read_test.csv")
read_obj.readFile()
print( read_obj.getFileContent() )

read_obj2 = File_read("Test_Data/", "read_test.csv")
print( "#" + read_obj2.getFileContent() + "#" )
read_obj2.readFile_line()
print( read_obj2.getFileContent() )

