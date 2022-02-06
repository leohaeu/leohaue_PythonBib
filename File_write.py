
###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### IMPORT

import string

from File_super import File_super

###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### CLASS


class File_write(File_super):

    def writeFileAppend(self, input : string):
        '''
        input: string
        "a"=append, "w"=overwrite
        '''
        f = open( self.getPathFileName() , "a")
        f.write( input )
        f.close()

    def writeFileOverwrite(self, input : string) :
        '''
        input: string
        "w"=overwrite (ueberschreiben)
        '''
        f = open( self.getPathFileName() , "a")
        f.write( input )
        f.close()



###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### TEST