import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from waiterclass import Waiter
from customerclass import Customer
from menuold import menu

class Orders:
    
    def __init__(self):
        self.waiter = Waiter()
        self.menu = menu()
        self.__fileName = "orders.json"
        self.getOrdersFromFile()

    def welcomeCustomer(self, custName):
        if custName in self.__orders:
            self.waiter.say(f"Welcome back to our restaurant {custName}!")
        else:
            self.waiter.say(f"I see this is your first time visiting our restaurant {custName}, please enjoy!")
    
    def storeOrdersToFile(self):
        with open(self.__fileName, 'w') as f:
            json.dump(self.__orders, f)
            
    def getOrdersFromFile(self):
        try:
            with open(self.__fileName, 'r') as f:
                self.__orders = json.load(f)
        except FileNotFoundError:
            self.__orders = {}
            
    def displayOrdersForCust(self, custName):
        if custName not in self.__orders:
            self.waiter.say(f"{custName} it appears you are a new customer and have no previous orders, please start an order.")
            self.Waiter.say("Here is the menu to help with your order. Please order at least three dishes. Once you have finished your order simply type 'finish'.")
            self.Waiter.say("The part of the menu corresponding to the course you chose will be shown to you.")
            self.getOrderFromCustomer(custName)
            self.storeOrdersToFile()
        else:
            orderList = self.__orders[custName]
            print()
            print(f"Customer: {custName}")
            for order in orderList:
                print()
                print(f"Order Number: {order}")
                orderItems = []
                orderSum = []
                orderItems.append(orderList[order])
                for item in orderList[order]:
                    orderItemList = self.menu.returnFoodItems()
                    orderItemIndex = orderItemList.index(item)
                    orderItemPrice = self.menu.returnFoodPrices()
                    orderSum.append(orderItemPrice[orderItemIndex])
                    orderSumTotal = sum(orderSum)
                print(f"Order Total: ${orderSumTotal}")
                for choice in orderList[order]:
                    print(f"> {choice} ${self.menu.getPrice(choice)}")
            print()
            self.waiter.say(f"These are all the stored previous orders for {custName}")
            print()

    def displayOrders(self, custName):
        print("Order History")
        if self.__orders:
            if custName:
                self.displayOrdersForCust(custName)
            else: 
                for custName in self.__orders:
                    self.displayOrdersForCust(custName)
        else:
            print("No Orders Found")

    def insertOrder(self, custName, choices):
        # existing orders exists
        if custName in self.__orders:
            orderList = self.__orders[custName]
            nextOrder = len(orderList) + 1
        #New customer
        else: 
            orderList = {}
            nextOrder = 1
        orderList[nextOrder] = choices
        self.__orders[custName] = orderList
        print(f"Order has been saved for {custName}")
        
        #input some data
        
    def getOrderFromCustomer(self, custName):
        choices = []
        orderTotal = []
        while True:
            course = self.waiter.listenFuzzy("What course would you like to order from?: ", listValue=["Starter", "Main", "Dessert", "Side", "finish"])
            if course[0] == "finish":
                choicesLength = len(choices)
                if choicesLength >= 3:
                    orderTotalInt = map(int, orderTotal)
                    orderTotalShown = sum(orderTotalInt)
                    break
                else:
                    self.waiter.say("You have not selected the correct amount of dishes please order 3 dishes.")
                    continue
            if course[1] < 60:
                self.waiter.say("Im sorry, I don't quite understand please enter your course again.")
            if course[0] == "Starter" and course[1] >= 80:
                self.waiter.printStarters()
                choice = self.waiter.listenFuzzy(f"{custName.title()}, what would you like to order from the starters?: ", listValue=["Garlic Naan", "Cheesy Garlic Naan", "Cheesy Mince Garlic Naan"])
                if choice[1] < 60: 
                    self.waiter.say("Im sorry, I dont quite understand please enter your choice for the starter course again.")
                if choice[0] == "Garlic Naan" or "Cheesy Garlic Naan" or "Cheesy Mince Garlic Naan" and choice[1] >= 60:
                    self.checkMeal(choice, menu, course)
                    choices.append(choice[0])
                    orderTotal.append(self.menu.getPrice(choice[0]))
                    self.waiter.say(f"You have selected {choice[0]} for your starter course. This meal costs ${int(self.menu.getPrice(choice[0]))}.")                           
            if course[0] == "Main" and course[1] >= 60:
                self.waiter.printMain()
                choice = self.waiter.listenFuzzy(f"{custName.title()}, what would you like to order from the mains?: ", listValue=["Butter Chicken", "Beef Vindalu", "Roganjosh"])
                if choice[1] < 60: 
                    self.waiter.say("Im sorry, I dont quite understand please enter your choice for the main course again.")
                if choice[0] == "Butter Chicken" or "Beef Vindalu" or "Roganjosh" and choice[1] >= 80:
                    self.checkMeal(choice, menu, course)
                    choices.append(choice[0])
                    orderTotal.append(self.menu.getPrice(choice[0]))
                    self.waiter.say(f"You have selected {choice[0]} for your main course. This meal costs ${int(self.menu.getPrice(choice[0]))}.")                           
            if course[0] == "Dessert" and course[1] >= 60:
                self.waiter.printDessert()
                choice = self.waiter.listenFuzzy(f"{custName.title()}, what would you like to order from the desserts?: ", listValue=["Gulab Jamun", "Jalebi"])
                if choice[1] < 60: 
                    self.waiter.say("Im sorry, I dont quite understand please enter your choice for the dessert course again.")
                if choice[0] == "Gulab Jamun" or "Jalebi" and choice[1] >= 60:
                    self.checkMeal(choice, menu, course)
                    choices.append(choice[0])
                    orderTotal.append(self.menu.getPrice(choice[0]))
                    self.waiter.say(f"You have selected {choice[0]} for your dessert course. This meal costs ${int(self.menu.getPrice(choice[0]))}.")                              
            if course[0] == "Side" and course[1] >= 60:
                self.waiter.printSide()
                choice = self.waiter.listenFuzzy(f"{custName.title()}, what would you like to order from the sides?: ", listValue=["Rice", "Papadams"])
                if choice[1] < 60: 
                    self.waiter.say("Im sorry, I dont quite understand please enter your choice for the side course again.")
                if choice[0] == "Rice" or "Papadams" and choice[1] >= 60:
                    self.checkMeal(choice, menu, course)
                    choices.append(choice[0])
                    orderTotal.append(self.menu.getPrice(choice[0]))
                    self.waiter.say(f"You have selected {choice[0]} for your side course. This meal costs ${int(self.menu.getPrice(choice[0]))}.")                             
        self.waiter.say(f"You have ordered:")
        for meal in choices:
            self.waiter.say(f">{meal} which costs ${int(self.menu.getPrice(meal))}.")
        self.waiter.say(f"Your order comes to a total of {orderTotalShown} dollars.")
        orderConfirmation = self.waiter.listenFuzzy("Are you sure you want to confirm and pay for your order? ", listValue=["yes", "no"])
        if orderConfirmation[0] == "yes" and orderConfirmation[1] >= 60:
            pass
        else:
            self.waiter.say("You have chosen to abandon your order. Thank you for dining with us.")
            exit()
        self.insertOrder(custName, choices)
        print()        
    
    def checkMeal(self, choice, menu, course): 
        total = 0 
        for course in list(self.menu.returnMenu().keys()): 
            if choice in list(self.menu.returnMenu()[course].keys()): 
                total += choice[course][choice] 
            else: pass        