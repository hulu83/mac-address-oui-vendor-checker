# /$$                 /$$
# | $$                | $$
# | $$$$$$$  /$$   /$$| $$ /$$   /$$
# | $$__  $$| $$  | $$| $$| $$  | $$
# | $$  \ $$| $$  | $$| $$| $$  | $$
# | $$  | $$| $$  | $$| $$| $$  | $$
# | $$  | $$|  $$$$$$/| $$|  $$$$$$/
# |__/  |__/ \______/ |__/ \______/

# Mac.vendor.search v1 created 08.2025  ( ﾉ ﾟｰﾟ)ﾉ
# Parsing clipboard.data // huluman83@gmail.com

# Explanation ##################################################################################################################
# Class Clipboard gets every Clipboard content with the pyperclip.module and hands it over to MacRegex                         #
# Class MacRegex checks for all Valid Mac-Adresses with following format XX: & XX- in full lenght! not only the first 3 Bytes. #
#                                                                                                                              #
# MacRegex.checkForMac() just Call! no return-value                                                                            #
# MacRegex.createMACSet() returns a Set filled with macs in upper-case                                                         #
#                                                                                                                              #
# Class VendorOUI creates a Vendor Dict-Obj out of >> standards-oui.ieee.org/oui/oui.txt >>                                    #
# VendorOUI.loadUI() check for !file create one                                                                                #
# VendorOUI.parseOUIFile() return vendor-dict obj.                                                                             #
# ##############################################################################################################################

# Import neccessary classes
from macmodules import classClipboard
from macmodules import classMacRegex
from macmodules import classOUI

# Create Instances and fire up _init_ methods!
clipBoardData = classClipboard.Clipboard()
regEX = classMacRegex.MacRegex(clipBoardData.getClipboard())
getOUI = classOUI.VendorOUI("https://standards-oui.ieee.org/oui/oui.txt")


# Check for all
# regEX.checkForMac()
macs = regEX.createMACSet()
# print(macs)


# OUI Part LOADFile If not exists -> create
#getOUI.updateOUIDB()
getOUI.loadOUI()

# Downlaod the OUI Vendor-List from IEEE and store into oui.txt. Parse with REGEX and return DICT! grouped by oui/vendor!
vendorDict = getOUI.parseOUIFile()
# print(vendorDict)

# Loop the SET-Object from Instance mac.Regex and handover as string and the Dict-Object from getOUI-Object!
for mac in macs:
    print(f"{mac} -> {getOUI.lookupVendor(mac, vendorDict)}")
