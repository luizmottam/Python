import os

def esp():
    print("{:=^30}".format(""))

tc = ["Teoria da Computação", 5, 0]
pi = ["Projeto Integrador", 0, 0]
ac = ["Arquitetura de Computadores", 5.63, 0]
oc = ["Organização de Computadores", 6.3, 0]
c2 = ["Cálculo II", 3.45, 0]
es = ["Estrutura de Dados", 0, 0]
mp = ["Metodologia de pesquisa", 1.73, 0]

materias = [tc, pi, ac, oc, c2, es, mp]
os.system('cls') or None

meta = float(input("Qual é a meta de pontos? "))

esp()
for i in range(0, 7):

    if materias[i][1] == 0:
        print("Sem nota ainda")
        esp()

    else:
        print(materias[i][0])
        print(f"P1: {materias[i][1]}")

        conta = (meta-((materias[i][1]) * 0.4))/0.6
        print(f"Nota para a P2: {conta:.2f}")
        esp()