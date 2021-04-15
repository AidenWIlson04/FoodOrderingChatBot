import pyttsx3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import spacy
import json
nlp = spacy.load("en_core_web_md")  
  
entireMenu = []  

class Waiter:
    
    def initVoice(self):
        '''
        Method: Initialise Text to Speech
        '''
        self.__engine = pyttsx3.init()

##        ''' Set Voice '''
        self.__voices = self.__engine.getProperty('voices')
        self.__vix = 1  # Male, 1 Female
        self.__voice = self.__voices[self.__vix].id
        self.__engine.setProperty('voice', self.__voice)

        ''' Set Rate '''
        self.__engine.setProperty('rate', 600)

        ''' Set Volume '''
        self.__engine.setProperty('volume', 1.0)

    def __init__(self, name="India Bot"):       
        self.__name = name
        self.initVoice()        
        self.say(f"Hello, Welcome to {name}, the best curry house in all the lands.")
        custName = self.askGuestName()  
        yesNo = ['Yes', 'No']        
        isName = self.listen(f"Is {custName} your name?: ")
        match, confidence = process.extractOne(isName, yesNo) 
        if confidence >= 60 and match == "Yes":
            pass
        else:
            while True:
                custName = self.repeatName()
                said = self.listen(f"Is {custName} your name?: ")
                match, confidence = process.extractOne(said, yesNo) 
                if confidence >= 60 and match == "Yes":
                    self.say(f"Welcome to our resteraunt {custName}")
                    break               
 
        what = self.listen("What do you want to do, see the menu, see previous orders or order food?: ")
        
        

    def say(self, words):
        pyttsx3.speak(words)
        print(words, end="")
        
    def say(self, words, printFlag=True):
        if printFlag:
            print(words)
        self.__engine.say(words, self.getName())
        self.__engine.runAndWait()
        
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def introduce(self):
        self.say(f"Hello, Welcome to {self.getName()}, the best curry house in all the lands.")
        print("/n")
          
    def printMenu(self):
        json_file = open("JSON\menu.json", "r", encoding="utf-8")
        file = json.load(json_file)
        json_file.close()
        self.__jsonMenu = file["menu"]      
        for category in self.__jsonMenu:
            print (f"======={category}========")
            for menuItem in self.__jsonMenu[category]:
                print (menuItem+':', '$' +str(self.__jsonMenu[category][menuItem]))
            print(" ")


    def listen(self, prompt ="I am listening, please speak:"):
        self.say(prompt, False)
        words = input(prompt)
        return words
    
    def askGuestName(self):
        name = self.listen("Please enter your name so that I can see if you have dined here before: ") 
        name = self.getGuestName(name)      
        return name

    def repeatName(self):
        name = self.listen("Please repeat your name: ")
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
        

if __name__ == '__main__':
    Waiter()


