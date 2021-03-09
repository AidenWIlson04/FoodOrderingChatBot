import spacy
nlp = spacy.load("en_core_web_sm")

def getName(speech):
        name = []
        doc = self.__nlp(speech.title()+" And")

        # Parts of Speech (POS) Tagging
        for token in doc:
            #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
            if token.pos_ in ["PROPN"]:
                #print("found one")
                name.append(token.text)

        name = " ".join(name)
        #print(f" 2: {name}")
        return name

name = getName('Hello my name is john')
print(name)