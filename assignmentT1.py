import pyttsx3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
    
class Waiter:
    
    def initVoice(self):
        '''
        Method: Initialise Text to Speech
        '''
        self.__engine = pyttsx3.init()

##        ''' Set Voice '''
        self.__voices = self.__engine.getProperty('voices')
        self.__vix = 0  # Male, 1 Female
        self.__voice = self.__voices[self.__vix].id
        self.__engine.setProperty('voice', self.__voice)

        ''' Set Rate '''
        self.__engine.setProperty('rate', 200)

        ''' Set Volume '''
        self.__engine.setProperty('volume', 1.0)

    def __init__(self, name="Gazza"):
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
     #   '''
     #   Avatar introduces themselves
     #   '''
        self.say(f"Hello. My name is {self.getName()}, welcome to the True Blue Aussie Dining Swag")


    def listen(self, prompt="I am listening, please speak:"):
        words = input(prompt)
        return words

waiter = Waiter()
waiter.introduce() 
previousGuestsDict = {}
previousGuests = True
while previousGuests:
    guestName = input("What is your full name?: ")
    previousGuestsDict = guestName
    previousGuests = False

waiter.say(f"Welcome {guestName}")

print(previousGuestsDict)


#class Guest:
    
   # def __init__(self, name = input("What is your name?: ")):
    #    self.__name = name
  
  
  
    
    
    
    
#Make program add guests name to dictionary at end of program.


