# 30/12/2022

Vogais = ["A","E","I","O","U"," "] 
Cifra = [" ","U","O","I","E","A"] 
frase = str.upper(input("Forme uma frase: ")) 
fraseCuringa = list(frase) 
for i in range(len(fraseCuringa)):     
    if fraseCuringa[i] in Vogais:         
       fraseCuringa[i] = Cifra[Vogais.index(fraseCuringa[i])] 
print("\n") 
fraseCuringa= "".join(fraseCuringa) 
print("sua frase criptografada: ",fraseCuringa)