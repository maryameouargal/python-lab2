#analyse de texte 

texte = input("Entrez un mot ou une phrase : ")
#les chooses à analyser 
longueur = len(texte)
majuscules = texte.upper()
minuscules = texte.lower()
inverse = texte[::-1]

# les resultats
print(f"Longueur du texte : {longueur}")
print(f"En majuscules : {majuscules}")
print(f"En minuscules : {minuscules}")
print(f"À l'envers : {inverse}")

print(f"Texte original : '{texte}'")