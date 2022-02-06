###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### IMPORT

import re
import os
import string


###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### CLASS

class String_manipulation():
    
    def __init__(self, origString : string) -> None:
        self.originalString: string
        self.originalString = origString
        self.manipulatedString: string

    def getOriginalString(self) -> string:
        return self.originalString

    def setManipulatedString(self, changedString: string) -> None:
        self.manipulatedString = changedString

    def getManipulatedString(self) -> string:
        return self.manipulatedString

    ###+++###+++###+++###
    # Manipulation

    def kommaToDot_betweenNumbers(self) -> None:
        origString = self.getOriginalString()
        self.setManipulatedString( re.sub('(?<=\d),(?=\d)', '.', origString) )
        

###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### TEST

'''
string_manipulation_obj = String_manipulation("Das ist die Testzahl: 21,34 | Ausserdem befindet sich hier , ein komma und eine zweite Zahl 45,67 ")
string_manipulation_obj.kommaToDot_betweenNumbers()
print(string_manipulation_obj.getOriginalString() )
print(string_manipulation_obj.getManipulatedString() )
'''