from fuzzywuzzy import fuzz
from fuzzywuzzy import process


validoptions = ["Order", "pizza", "menu", "exit", "ice cream", "soup"]
#validoptions = ["yes", "no"]

choices = []
exit = False
while True:
    query = input(f'{" or ".join(validoptions)}?: ')
    if not query:
        break
    
    (match, confidence) = process.extractOne(query, validoptions)
    
    print(f"{query}: matches: {match} at {confidence}%")

