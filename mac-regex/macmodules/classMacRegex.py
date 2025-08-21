import re

class MacRegex:

    # init clipboard data and create regex-pattern
    def __init__(self, data) -> None:
        self.data = data
        self.regExPattern = r'([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})|([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2})'

    # Check Data for MAC-Address occurences
    def checkForMac(self) -> None: 
        self.occurence = re.search(self.regExPattern, self.data)
        
        if(self.occurence):
            print("Valid Mac-Address")
        else: print("No valid Mac-Address")
    
    # View PyperClip Data
    def viewData(self): 
        print(self.data)

    def createMACSet(self) ->set:
        
        # Create Set-Object - Sets doesn't allow duplicates!
        x = self.macSet = set()

        # Loop for matches and store it
        for self.matches in re.finditer(self.regExPattern, self.data): 
         x.add(self.matches.group().upper())
         print("Macs hinzugefügt: ",self.matches.group())
        return x
            
            
        
        

