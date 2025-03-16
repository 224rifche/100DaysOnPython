print("Donner deux varibles " )
var1 = int(input("Donner la variable A : "))
var2 = int(input("Donner la variable B : "))

print("**************Avant echanges *************")
print(f"La valeur de A {var1}")
print(f"La valeur de B {var2}")

var1 = var1 + var2 
var2 = var1 - var2
var1 = var1 - var2

print("************Après echanges ***************")
print(f"La valeur A de {var1}")
print(f"La valeur B de {var2}")
