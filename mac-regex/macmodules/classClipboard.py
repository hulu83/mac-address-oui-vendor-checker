import pyperclip

class Clipboard:
    def __init__(self):
        pass
    
    def getClipboard(self):
        return pyperclip.paste()
