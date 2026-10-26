

class TextAnalyzer:
    def __init__(self, text):
        if text == "":
         raise Exception("Text cannot be empty")       
        else:
           self.text = text
    def __str__(self):
       pass