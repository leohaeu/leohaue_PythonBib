###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### IMPORT

import re
import os
import string


###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### CLASS

class Strin_manipulation():
    
    def __init__(self, inString) -> None:
        self.inputString: string
        self.inputString = inString
        self.outputString: string
        self.outputString = None

    def getInString(self) -> string:
        return self.inputString

    def setOutString(self, changedString: string) -> None:
        self.outputString = changedString

    def getOutString(self) -> string:
        return self.outputString

    ###+++###+++###+++###
    # Manipulation

    def kommaToDot_betweenNumbers(self) -> None:
        inString = self.getInString()
        self.setOutString( re.sub('(?<=\d),(?=\d)', '.', inString) )
        

###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### TEST

string_manipulation_obj = Strin_manipulation("Das ist die Testzahl: 21,34 | Ausserdem bfindet sich hier , ein komma und eine zweite Zahl 45,67 ")
string_manipulation_obj.kommaToDot_betweenNumbers()
print(string_manipulation_obj.getInString() )
print(string_manipulation_obj.getOutString() )