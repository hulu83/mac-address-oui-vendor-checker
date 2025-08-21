import re
import requests
import os
from datetime import datetime, timedelta
from pathlib import Path


class VendorOUI:

    def __init__(self, vendorListURL:str) -> None:
        # create time obj for file
        self.m_time = os.path
        self.bestBefore = timedelta(days=7)
        self.dateTimeToday = datetime.now()
        
        # Set vendorList-Obj and bufferFile -> out.txt
        self.vendorListURL = vendorListURL
        self.bufferFile = Path("oui.txt")

        # NEEDED otherwise TEAPOT-ERROR 418!
        self.user_agent = {'User-agent': 'Mozilla/5.0'} 


    def updateOUIDB(self) -> None:
        print("Updating OUI DB")
        
        # make them wait!
        response = requests.get(self.vendorListURL,allow_redirects = True, timeout=30, headers = self.user_agent)

        # response.raise_for_status()
        with open(self.bufferFile, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        print(self.bufferFile)

    
    def loadOUI(self):
        # create timestamp and calculate creationdate + x-Days like defined in _init_ to recreate the file to stay updated
        self.timeStamp = self.m_time.getmtime("oui.txt")

        # convert timestamp into DateTime object
        cDateTime = datetime.fromtimestamp(self.timeStamp)
        self.bestBefore = cDateTime + self.bestBefore
        
        # print("AblaufDatum!: ", self.bestBefore)
        # print("Created: ", cDateTime)
        # print("DateTime NOW: ", self.dateTimeToday)

        if not self.bufferFile.exists() or self.dateTimeToday > self.bestBefore:
            self.updateOUIDB()

    
    def parseOUIFile(self) -> dict:
        self.ouiDict = {}

        # Regex through File and Group by oui and vendor. Nice SHIT! ;)
        ouiRegex = re.compile(r"^(?P<oui>[0-9A-F]{6})\s+\(base 16\)\s+(?P<vendor>.+)$")

        with open(self.bufferFile, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                x = ouiRegex.match(line.strip())
                if x:
                    self.ouiDict[x.group("oui")] = x.group("vendor").strip()
        return self.ouiDict
    
    
    def lookupVendor(self, macs:str, vendorDB:dict) -> str:
        # Remove everything NON-HEX!
        macRemoveNoneHex = re.sub(r'[^0-9A-F]', '', macs)
    
        #Only first 6 Chars
        macHexOnly = macRemoveNoneHex[:6]

        #print(macHexOnly)
        return vendorDB.get(macHexOnly, "No Vendor Found -> Check MACS")


