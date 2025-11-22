#programme de calculatrice 

#menu 
print("1-addition\n")
print("2-soustraction\n")
print("3-mutliplication \n")
print("4-division\n")
#option 
option = int(input(" entrer le nombre de l'opération choissit  : "))
resultat = 0 
#les opérations 
if (option in [1,2,3,4]): 
   num1 = float(input("entre le premier nombre:")) 
   num2 = float(input("entre le deuxième nombre:")) 
   if (option == 1):
       resultat = num1+num2
   elif (option == 2):
       resultat = num1-num2
   elif (option == 3):
       resultat = num1*num2
   elif (option == 4):
        if num2 != 0:
         resultat = num1/num2
        else:
           print("Erreur : division par zéro !")
else: 
    print("opération invalide")

print("le resultat de l'opération est {}".format(resultat))