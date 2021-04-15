from ordersclass import Orders
from waiterclass import Waiter
from customerclass import Customer
from menuold import menu
import pyttsx3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import spacy
import json
nlp = spacy.load("en_core_web_md")  
  

class Chatbot:
    
    def __init__(self, name="India Bot"): 
        self.Waiter = Waiter()
        self.Orders = Orders()
        self.Customer = Customer()
        self.Menu = menu()
        self.__name = name
        self.Waiter.initVoice()          
        self.Waiter.say(f"Hello, Welcome to {name}, the best curry house in all the lands.")
        custName = self.Customer.customerNameMain()
        self.__custName = custName
        self.chatbotMain()
                 
    def chatbotMain(self):
        action = self.Waiter.listen("What do you want to do, see the menu, see previous orders, order food or exit?: ")
        validAction = ["menu", "previous", "order", "exit"]
        match, confidence = process.extractOne(action, validAction)
        while True: 
            if confidence < 80:
                self.Waiter.say("I'm sorry, I don't quite understand, Please try again.")
                action = self.Waiter.listen("What do you want to do, see the menu, see previous orders, order food or exit?: ")
                validAction = ["menu", "previous", "order", "exit"]
                match, confidence = process.extractOne(action, validAction)
            break 
        if confidence >= 80 and match == "menu":
            while True:
                menuPart = self.Waiter.listen("Do you want to see the starter's, main's, dessert's, sides, the whole menu see previous orders or order?: ")
                validMenuPart = ["starter", "main", "dessert", "side", "whole", "previous", "order"]
                match, confidence = process.extractOne(menuPart, validMenuPart)
                if confidence >= 80 and match =="starter":  
                    self.Waiter.printStarters()
                elif confidence >= 80 and match =="main":
                    self.Waiter.printMain()
                elif confidence >= 80 and match =="dessert":
                    self.Waiter.printDessert()
                elif confidence >= 80 and match =="side":
                    self.Waiter.printSide()
                elif confidence >= 80 and match == "whole":
                    self.Waiter.printMenu() 
                elif confidence >= 80 and match == "previous" or "order":
                    break
        if confidence >= 80 and match == "previous":
            self.Orders.getOrdersFromFile()
            self.Orders.displayOrdersForCust(self.__custName)
        if confidence >= 80 and match == "order":
            self.Waiter.printMenu()
            self.Waiter.say("Here is the menu to help with your order. Please order at least three dishes. Once you have finished your order simply type 'finish'.")
            self.Orders.getOrderFromCustomer(self.__custName)
            self.Orders.storeOrdersToFile()
        if confidence >= 80 and match == "exit":
            self.Waiter.say("Thank you for dining with us.")
            exit()
def main():
    Chatbot() 
    
if __name__ == '__main__':
    main()




