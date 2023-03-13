def chiffrement_cesar(msg, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = ""
    phrase = ""
    message = msg.lower()
    for i in message:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                if i == "a":
                    letter = "z"
                elif i == "z":
                    letter = "a"
                else:
                    letter = alphabet[j + decalage]
        phrase +=letter
    print(phrase)








chiffrement_cesar('bonjour', 3)