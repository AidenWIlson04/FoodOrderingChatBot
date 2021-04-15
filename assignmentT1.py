from ordersclass import Orders
import pyttsx3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import spacy
import json
nlp = spacy.load("en_core_web_md")  


entireMenu = []  

class Waiter:
    
    def initVoice(self):
        self.__engine = pyttsx3.init()

        self.__voices = self.__engine.getProperty('voices')
        self.__vix = 1  
        self.__voice = self.__voices[self.__vix].id
        self.__engine.setProperty('voice', self.__voice)

        self.__engine.setProperty('rate', 999)

        self.__engine.setProperty('volume', 1.0)

    def __init__(self, name="India Bot"): 
        self.__name = name
        self.initVoice()          
        self.say(f"Hello, Welcome to {name}, the best curry house in all the lands.")
        self.customerNameMain()
        self.chatbotMain()
        self.Orders = Orders(Waiter) 
        
    
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
   
    def customerNameMain(self):
        custName = self.askGuestName()  
        yesNo = ['Yes', 'No']        
        isName = self.listen(f"So your name is {custName}?: ")
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
    
    def chatbotMain(self):
        action = self.listen("What do you want to do, see the menu, see previous orders or order food?: ")
        validAction = ["menu", "previous", "order"]
        match, confidence = process.extractOne(action, validAction)
        while True: 
            if confidence < 80:
                self.say("I'm sorry, I don't quite understand, Please try again.")
                action = self.listen("What do you want to do, see the menu, see previous orders or order food?: ")
                validAction = ["menu", "previous", "order"]
                match, confidence = process.extractOne(action, validAction)
            break 
        if confidence >= 80 and match == "menu":
            menuPart = self.listen("Do you want to see the starter's, main's, dessert's, sides or the whole menu?: ")
            validMenuPart = ["starter", "main", "dessert", "side", "whole"]
            match, confidence = process.extractOne(menuPart, validMenuPart)
            if confidence >= 80 and match =="starter":  
                self.printStarters()
            elif confidence >= 80 and match =="main":
                self.printMain()
            elif confidence >= 80 and match =="dessert":
                self.printDessert()
            elif confidence >= 80 and match =="side":
                self.printSide()
            elif confidence >= 80 and match == "whole":
                self.printMenu() 
        if confidence >= 80 and match == "previous":
            self.Orders.getOrdersFromFile()
            self.Orders.insertOrder()
            self.Orders.displayOrdersForCust()
        if confidence >= 80 and match == "order":
            self.Orders.getOrderFromCustomer()
            self.Orders.storeOrdersToFile()
            
            


if __name__ == '__main__':
    Waiter()













             
'''        
        secAction = self.listen("What would you like to do now? You can see previous orders, order food or go back through the menu: ")         
        validSecAction = ["previous", "order", "menu"]
        match, confidence = process.extractOne(secAction, validSecAction)
        while True:
            if confidence < 80:
                self.say("I'm sorry, I don't quite understand, Please try again.")
                secAction = self.listen("What would you like to do now? You can see previous orders, order food or go back through the menu: ")         
                validSecAction = ["previous", "order", "menu"]
                match, confidence = process.extractOne(secAction, validSecAction)
            break
        if confidence >= 80 and match == "menu":
            self.printMenu()
        if confidence >= 80 and match == "order":
            menuSection = self.listen("What section of the menu would you like to order from?: ")
            validMenuSection = ["starter", "main", "dessert", "side"]
            match, confidence = process.extractOne(menuSection, validMenuSection)
'''       
        
    
    