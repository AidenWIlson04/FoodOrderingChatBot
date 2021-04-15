import json

class menu:
    
    def __init__(self):
        self.jsonMenu = self.returnMenu()["menu"]
    
    def getPrice(self, choice):
        mealPrice = []
        if choice in self.returnFoodItems():
            return self.returnFoodPrices()[self.returnFoodItems().index(choice)]

    def sumOfNumList(self, numList):
        #numList = []
        listTotalInt = map(int, numList)
        listTotalShown = sum(listTotalInt)
        return listTotalShown
        
    def returnFoodItems(self):
        finalList = []
        for category in self.jsonMenu:
            for food in self.jsonMenu[category]:
                finalList.append(food)
        return finalList

    def returnFoodPrices(self):
        finalList = []
        for category in self.jsonMenu:
            for food in self.jsonMenu[category]:
                finalList.append(self.jsonMenu[category][food])
        return finalList
    
    def returnMenu(self):
        try:
            with open("JSON/menu.json", 'r') as f:
                self.__menu = json.load(f)
        except FileNotFoundError:
            self.__menu = {}
        return self.__menu

    def menu(self):
         menu ={
    "Starter" :
    {
        "Garlic Naan : 3.00",
        "Cheesy Garlic Naan : 4.00",
        "Cheesy Mince Garlic Naan : 8.00"
    },
    "Main" :
    {
        "Butter Chicken : 17.00",
        "Beef Vindalu : 20.00",
        "Roganjosh : 20.00"
    },
    "Dessert" :
    {
        "Gulab Jamun : 4.00",
        "Jalebi : 4.00"
    },
    "Side" :
    {
        "Rice : 3.00",
        "Papadams : 1.00"
        
    }
    }  
         