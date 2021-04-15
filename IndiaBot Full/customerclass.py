import pyttsx3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import spacy
import json
nlp = spacy.load("en_core_web_md")  
from waiterclass import Waiter

class Customer:
    
    def __init__(self):
        self.__engine = pyttsx3.init()
        self.waiter = Waiter()
         
    def listen(self, prompt="I am listening, please speak:"):
        words = input(prompt)
        return words
    
    def say(self, words):
        self.say(words, True)
    
    def say(self, words, printFlag=True):
        if printFlag:
            print(words)
        self.__engine.say(words, self.waiter.getName())
        self.__engine.runAndWait()
    
    def askGuestName(self):
        name = self.waiter.listen("Please enter your name: ")
        name = self.getGuestName(name)      
        return name

    def repeatName(self):
        name = self.waiter.listen("Please repeat your name: ")
        name = self.getGuestName(name)
        return name
    
    def getGuestName(self, speech):
        name = []
        doc = nlp(speech.title()+" And")
        for token in doc:
              if token.pos_ in ["PROPN"]:
                  name.append(token.text)
        name = " ".join(name)        
        return name
    
    def customerNameMain(self):
        custName = self.askGuestName()  
        yesNo = ['Yes', 'No']        
        isName = self.waiter.listen(f"Your name is {custName}, is this correct?: ")
        match, confidence = process.extractOne(isName, yesNo) 
        if confidence >= 60 and match == "Yes":
            pass
        else:
            while True:
                custName = self.repeatName()
                said = self.listen(f"Is {custName} your name?: ")
                match, confidence = process.extractOne(said, yesNo) 
                if confidence >= 60 and match == "Yes":
                    break 
        return custName
    