print ("Olá, gostaria de saber qual é o seu signo?,")
print ("Digite tudo em letras minusculas por favor!!")

mes1 = "março"
mes2 = "abril"
mes3 = "maio"
mes4 = "junho"
mes5 = "julho"
mes6 = "agosto"
mes7 = "setembro"
mes8 = "outubro"
mes9 = "novembro"
mes10 = "dezembro"
mes11 = "janeiro"
mes12 = "fevereiro"

x = int(input ("Digite seu dia de nascimento com 2 digitos: "))
y = (input ("Escreva o nome do mês de nascimento: "))
print ("Certo, você nasceu no dia: ",x ,"no mês de: ", y)

if x>=20 and x<=31 and y==mes1:
    print ("aries")
if x>=20 and x <=30 and y==mes2 or x>=1 and x<=20 and y==mes3:
        print("touro")
if x>=20 and x<=31 and y==mes3 or x>=1 and x<=20 and y==mes4:
    print ("gemeos")
if x>=21 and x<=30 and y==mes4 or x>=1 and x<=21 and y==mes5:
    print ("cancer")
if x>=22 and x<=31 and y==mes5 or x>=1 and x<=22 and y==mes6:
    print ("leão")
if x>=23 and x<=31 and y==mes6 or x>=1 and x<=22 and y==mes7:
    print ("virgem")
if x>=23 and x<=30 and y==mes7 or x>=1 and x<=22 and y==mes8:
    print ("libra")
if x>=23 and x<=31 and y==mes8 or x>=1 and x<=22 and y==mes9:
    print ("escorpião")
if x>=23 and x<=30 and y==mes9 or x>=1 and x<=23 and y==mes10:
    print ("sagitario")
if x>=23 and x<=31 and y==mes10 or x>=1 and x<=20 and y==mes11:
    print ("capricornio")
if x>=21 and x<=31 and y==mes11 or x>=1 and x<=19 and y==mes12:
    print ("aquario")
if x>=20 and x<=29 and y==mes12 or x>=1 and x<=19 and y==mes1:
    print ("peixes")
