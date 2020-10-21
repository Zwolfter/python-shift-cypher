import re

class CShift:
    def __init__(self):
        self.regex = re.compile('[a-z]',re.I)
    
    def encode(self, str, factor):
        return self.shift(str, factor)
    
    def decode(self, str, factor):
        return self.shift(str, -(factor))

    def shift(self, str, factor):
        if factor < 0:
            return self.shift(str, (factor + 26))
        output = ""
        for c in str:
            oc =''
            if self.regex.match(c):
                code = ord(c)
                if code >= 65 and code <= 90:
                    newCode = (((code - 65 + factor) % 26) + 65)
                    oc = chr(newCode)
                if code >= 97 and code <= 122:
                    newCode = (((code - 97 + factor) % 26) + 97)
                    oc = chr(newCode)
            output += oc
        print(output)
        return(output)

