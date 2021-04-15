import pyttsx3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import spacy
import json
nlp = spacy.load("en_core_web_md")


class Waiter:

    def initVoice(self):
        self.__engine = pyttsx3.init()

        self.__voices = self.__engine.getProperty('voices')
        self.__vix = 1  
        self.__voice = self.__voices[self.__vix].id
        self.__engine.setProperty('voice', self.__voice)

        self.__engine.setProperty('rate', 200)

        self.__engine.setProperty('volume', 1.0)

    def __init__(self, name="IndiaBot"):
        self.__name = name
        self.initVoice()

    def say(self, words):
        self.say(words, True)

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
    
    def spell(self, word):
        for letter in word:
            self.say(letter)

    def listen(self, prompt="I am listening, please speak:"):
        words = input(prompt)
        return words
    
    def listenFuzzy(self, prompt="I am listening, please speak: ", listValue=[]):
        custWords = self.listen(prompt)
        match, confidence = process.extractOne(custWords, listValue)
        return(match, confidence)
        

    def printMenu(self):
        json_file = open("JSON\menu.json", "r", encoding="utf-8")
        file = json.load(json_file)
        json_file.close()
        self.__jsonMenu = file["menu"]      
        for category in self.__jsonMenu:
            print(" ")
            print (f"======={category}========")
            for menuItem in self.__jsonMenu[category]:
                print (menuItem+':', '$' +str(self.__jsonMenu[category][menuItem]))
            print(" ")

    def printStarters(self):
        json_file = open("JSON\menu.json", "r", encoding="utf-8")
        file = json.load(json_file)
        json_file.close()
        self.__jsonMenu = file["menu"]      
        print(" ")  
        print("=======Starters========")
        for menuItem in self.__jsonMenu["Starter"]:
            print (menuItem+':', '$' +str(self.__jsonMenu["Starter"][menuItem]))
        print(" ")  
    
    def printMain(self):
        json_file = open("JSON\menu.json", "r", encoding="utf-8")
        file = json.load(json_file)
        json_file.close()
        self.__jsonMenu = file["menu"]      
        print(" ")  
        print("=======Mains========")
        for menuItem in self.__jsonMenu["Main"]:
            print (menuItem+':', '$' +str(self.__jsonMenu["Main"][menuItem]))
        print(" ") 
        
    def printDessert(self):
        json_file = open("JSON\menu.json", "r", encoding="utf-8")
        file = json.load(json_file)
        json_file.close()
        self.__jsonMenu = file["menu"]      
        print(" ")  
        print("=======Desserts========")
        for menuItem in self.__jsonMenu["Dessert"]:
            print (menuItem+':', '$' +str(self.__jsonMenu["Dessert"][menuItem]))
        print(" ")
    
    def printSide(self):
        json_file = open("JSON\menu.json", "r", encoding="utf-8")
        file = json.load(json_file)
        json_file.close()
        self.__jsonMenu = file["menu"]      
        print(" ")  
        print("=======Sides========")
        for menuItem in self.__jsonMenu["Side"]:
            print (menuItem+':', '$' +str(self.__jsonMenu["Side"][menuItem]))
        print(" ")

    def listen(self, prompt ="I am listening, please speak:"):
        self.say(prompt, False)
        words = input(prompt)
        return words
