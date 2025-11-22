#programme de conversion de température

T = float(input("saisir la température en Celsius: "))

#T(°C)= (T(°F)-32*5/9
#T(°F)=T(°C)*9/5 + 32 
#T(°k)=kelvin = T(°C) + 273.15

#la converstion 
kelvin = T+ 273.15
fahrenheit = T*9/5 + 32 

#le resultat
print("la temperature {} en kelvin et {} en fahrenheit ".format( kelvin,fahrenheit )) 