
def est_palindrome(phrase):
     # supression d'espace et convertion en minuscule

    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace(".", "")
    phrase = phrase.replace(",", "")
    phrase = phrase.replace(":", "")
    phrase = phrase.replace(";", "")
    phrase = phrase.replace("!", "")
    phrase = phrase.replace("?", "")
    phrase = phrase.replace("/", "")
    phrase = phrase.replace("(", "")
    phrase = phrase.replace(")", "")
    phrase = phrase.replace("'", "")
    phrase = phrase.replace("*", "")
    phrase = phrase.replace("-", "")
    phrase = phrase.replace("_", "")
    phrase = phrase.replace("{", "")
    phrase = phrase.replace("}", "")
    phrase = phrase.replace("[", "")
    phrase = phrase.replace("]", "")
    phrase = phrase.replace("|", "")

    #on initialise les indices 
    debut = 0
    fin = len(phrase) - 1 

    #on lance la boucle de comparaison
    while debut < fin:
        if phrase[debut] != phrase[fin]:
            return False
        debut += 1
        fin -= 1
    
    # on retourne vrai si la boucle s'execute en entière
    return True
txt = input("Entrer un mot ou une phrase : ")
txt = str(txt)
value = est_palindrome(txt)
if value == True:
    print("Cette phrase est bien un palindrome !")
else:
    print("Cette phrase n'est pes un palindrome")