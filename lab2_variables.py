#etape 1
entier = 42              # int
flottant = 3.14          # float
texte = "Python"         # str
vrai_ou_faux = True      # bool

#etape 2
print(entier, "→", type(entier))
print(flottant, "→", type(flottant))
print(texte, "→", type(texte))
print(vrai_ou_faux, "→", type(vrai_ou_faux))

#etape 3
try:
    age = int(input("Quel âge as-tu ? "))
    print(f"Dans 5 ans tu auras {age + 5} ans.")
except ValueError: 
    print("Saisie invalide, merci d'entrer un entier.")
    
# etape 4
nombre = 10      # nombre référence un int
print(nombre)

nombre = 10 + 5  # le même nom nombre pointe désormais vers un autre int (15)
print(nombre)

#Teste des autres conversions
print(float("7.5"))      
print(bool("False"))     
print(str(1234))         