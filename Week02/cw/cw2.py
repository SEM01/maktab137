'''
Write a function that takes three list(names, verbs, adverbs)
and creates a random sentence.
'''


import random

def make_a_sentence(names,verbs,adverbs):
    name_choice = random.choice(names)
    verb_choice = random.choice(verbs)
    adverb_choice = random.choice(adverbs)
    sentence_generate =(
        "".join(name_choice)
        +" "+"".join(verb_choice)
        +" "+"".join(adverb_choice)
        )
    print(sentence_generate)


names = ["Ali","Reza","Majid"]
verbs = ["Khord","Poshid","Goft"]
adverbs = ["Ghaza","ketab","Lebas"]
make_a_sentence(names,verbs,adverbs)