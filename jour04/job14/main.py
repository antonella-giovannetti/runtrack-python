def length(el):
    count = 0
    for i in el:
        count+= 1
    return count

def add(liste, x):
    liste += [x]
    return liste

def separation(str):
    phrase = []
    mot = ""
    for i in str:
        if i != " ":
            mot += i
        else:
            add(phrase, mot)
            mot = " "
    return phrase

def my_long_word(n, str):
    list_of_words = separation(str)
    sentence = ""
    for i in list_of_words:
        if length(i) > n:
            sentence += i
            sentence += " "
    print(sentence)

my_long_word(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance")