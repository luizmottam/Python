import os
os.system('cls') or None

a1 = float(input("Nota do 1° Bimestre: "))

notafinal_b1 = a1 * 0.4
notaquefalta = (5 - notafinal_b1)/0.6
print(f"Para passar você precisa tirar {notaquefalta} pontos")
os.system('pause') or None
os.system('cls') or None


a2 = float(input("Nota do 2° Bimestre: "))

notafinal_b2 = a2 * 0.6
os.system('cls') or None
notafinal = notafinal_b1 + notafinal_b2
if (notafinal >= 4.98):
    print(f"VOCÊ PASSOU !!!\n\nNota final do 1° bimestre: {notafinal_b1}\nNota final do 2° bimestre: {notafinal_b2}\n Nota final: {notafinal}")

else:
    print(f"VOCÊ NÃO PASSOU\n\nNota final do 1° bimestre: {notafinal_b1}\nNota final do 2° bimestre: {notafinal_b2}\n Nota final: {notafinal}")