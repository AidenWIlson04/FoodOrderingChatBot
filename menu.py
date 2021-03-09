menu ={
"starter" :
    {
        "eggs" : 3.00,
        "toast" : 5.00
    },
"main" :
    {
        "steak" : 25.00,
        "squid" : 35.00,
        "Lobster" : 80.00
    },
"dessert" :
    {
        "gelato" : 5.00,
        "banana split" : 6.00
    }
}

print(menu["starter"])
meals = menu["starter"]
print(meals["eggs"])

while True:
    course = input("course")
    print(menu[course])
    for meal in menu[course]:
        print(meal, menu[course][meal])