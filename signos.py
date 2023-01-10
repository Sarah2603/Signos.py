# -*- coding: utf-8 -*-
import sys

def formatacao(dia, mes, signo):
    total = len(signo) + 6
    print(f"""
Certo, você nasceu no dia {dia} do mês de {mes}
Você é do signo de:

                {'#' * total}
                ## {signo} ##
                {'#' * total}
                    """)

def meses():
    mes = [ 
        "março",    # m[0]
        "abril",    # m[1]
        "maio",     # m[2]
        "junho",    # m[3]
        "julho",    # m[4]
        "agosto",   # m[5]
        "setembro", # m[6]
        "outubro",  # m[7]
        "novembro", # m[8]
        "dezembro", # m[9]
        "janeiro",  # m[10]
        "fevereiro" # m[11]
    ]
    return mes

def verificador(dia, mes=None):
    m = meses()

    # confere se a entrada da var dia, entrou somente valor do 1 ao 31
    if dia > 31 or dia < 1:
        print('Os dias válidos, do 1 ao 31')
        return True
    elif mes == None:
        return False

    # faz uma verificacao se o mes digitado está na lista da funcao meses()
    if mes not in m:
        print('\nmês de nascimento invalido')
        print('Lista de meses validos abaixo\n')

        # se não estiver na funcao meses()
        # ele mostra a lista de mês validos e encerra o programa
        for valido in m:
            print(valido)
        return True
    else:
        mes_trinta = [m[1], m[3], m[6], m[8]]

        # para garantir que os mês de 30 dias, nao tenha entrada de 31
        if mes in mes_trinta and dia > 30:
            print('Para esse mês, os dias válido são do 1 ao 30')
            return True

        # para garantir que o mês de fevereiro não tenha entrada maior que 29
        elif mes == m[11] and dia > 29:
            print('Para esse mês, os dias válido são do 1 ao 29')
            return True
        else:
            return False

def main():
    
    print ("Olá, gostaria de saber qual é o seu signo? ")

    # usando o try para que não tenha um erro grave com entrada de string ou float
    try:
        dia = int(input("Digite seu dia de nascimento: "))
        
        if verificador(dia):

            # se for digitado um valor inválido, será avisado sobre o erro e sairá
            sys.exit()
    except:
        print('ERROR. por favor, digite um número inteiro válido')
        sys.exit()
    try:
        mes = str(input("Escreva o nome do mês de seu nascimento: ")).lower().strip()

        if verificador(dia, mes):
            sys.exit()
        else:
            # se tudo estiver correto, será ativado a função calculo()
            calculo(dia, mes)
    except:
        pass
    
# calculo recebe da função main() o dia e mês do usuario
def calculo(dia, mes):
    m = meses()
    if dia>=20 and dia<=31 and mes==m[0] or dia>=1 and dia<=18 and mes==m[1]:
        formatacao(dia, mes, "Aries")
    elif dia>=19 and dia<=30 and mes==m[1] or dia>=1 and dia<=19 and mes==m[2]:
        formatacao(dia, mes, "Touro")
    elif dia>=20 and dia<=31 and mes==m[2] or dia>=1 and dia<=20 and mes==m[3]:
        formatacao(dia, mes, "Gemeos")
    elif dia>=21 and dia<=30 and mes==m[3] or dia>=1 and dia<=21 and mes==m[4]:
        formatacao(dia, mes, "Cancer")
    elif dia>=22 and dia<=31 and mes==m[4] or dia>=1 and dia<=22 and mes==m[5]:
        formatacao(dia, mes, "Leão")
    elif dia>=23 and dia<=31 and mes==m[5] or dia>=1 and dia<=21 and mes==m[6]:
        formatacao(dia, mes, "Virgem")
    elif dia>=22 and dia<=30 and mes==m[6] or dia>=1 and dia<=22 and mes==m[7]:
        formatacao(dia, mes, "Libra")
    elif dia>=23 and dia<=31 and mes==m[7] or dia>=1 and dia<=21 and mes==m[8]:
        formatacao(dia, mes, "Escorpião")
    elif dia>=22 and dia<=30 and mes==m[8] or dia>=1 and dia<=21 and mes==m[9]:
        formatacao(dia, mes, "Sagitario")
    elif dia>=21 and dia<=31 and mes==m[9] or dia>=1 and dia<=19 and mes==m[10]:
        formatacao(dia, mes, "Capricornio")
    elif dia>=20 and dia<=31 and mes==m[10] or dia>=1 and dia<=18 and mes==m[11]:
        formatacao(dia, mes, "Aquario")
    elif dia>=19 and dia<=29 and mes==m[11] or dia>=1 and dia<=19 and mes==m[0]:
        formatacao(dia, mes, "Peixes")

if __name__ == "__main__":
    main()