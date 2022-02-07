
###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### IMPORT

import string



###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### CLASS


class File_super():

    def __init__(self, pathN, fileN) -> None:
        self.pathName : string
        self.pathName = pathN
        self.fileName : string
        self.fileName = fileN
        self.fileContent : string
        self.fileContent = ""

    def getPathFileName(self) -> string:
        return self.pathName + self.fileName

    def setFileContent(self, content : string) -> None:
        self.fileContent = content

    def addFileContent(self, newContent : string) -> None: 
        self.fileContent = self.fileContent + newContent

    def getFileContent(self) -> string:
        return self.fileContent

    


###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### TEST


