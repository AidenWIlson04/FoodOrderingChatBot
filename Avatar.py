# pip install pywin32
# pip install pyttsx3    supports up to Python 3.9

import pyttsx3


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
        '''
        Avatar introduces themselves
        '''
        self.say(f"Hello. My name is {self.getName()}")

    def spell(self, word):
        for letter in word:
            self.say(letter)

    def listen(self, prompt="I am listening, please speak:"):
        words = input(prompt)
        return words

# Test harness that will only work as a standalone
#def main():
 #   test = Waiter()
  #  test.introduce()
  #  test.say("Hello")
   # test.spell("Hello")
   # test.say(test.listen())

# if __name__ == "__main__":
  #  main()

