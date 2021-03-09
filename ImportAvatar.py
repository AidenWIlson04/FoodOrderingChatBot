from Avatar import Avatar
from random import choice

class Charlie:

    def __init__(self):
        self.__words = ["apple", "pear", "pineapple", "banana"]
        self.charlie = Avatar("Charlie")
        self.charlie.say("Welcome to spell checker")
        
    def play(self):
        while True:
            action = self.charlie.listen("Do you want to play? ")
            if not action or action.lower().strip()[0] == 'n':
                self.charlie.say("Bye Bye")
                break
            word = choice(self.__words)
            self.charlie.say(f"Please spell {word}", False)
            guess = self.charlie.listen("Spell now: ")
            if guess!=word:
                self.charlie.listen("Spell now: ")
                attempts= 3
                correct = False
                while attempts>0 or not correct:
                    guess = self.charlie.listen("Spell now: ")
                    if guess==word:
                        correct=True
                        self.charlie.say("Yahoo! You got it right")
                    else: 
                        self.charlie.say("You got it wrong. You spelt it this way ")
                        self.charlie.spell(guess)
                        self.charlie.say("Try again")
                        
                        attempts -=1
                        
    

 


def main():
    c = Charlie()
    c.play()


if __name__ == "__main__":
    main()
