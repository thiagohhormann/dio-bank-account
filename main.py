menu = """

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

"""

deposits = ()
withdraws = ()

"""
3 saques diários, R$500 por saque
saldo atual ao fim do extrato: R$xxx.xx
"""

while True:
    user_input = input(menu)

    match term:
        case d:
            print('deposito')
        case s:
            print('saque') 
        case e:
            print('extrato') 
        case q:
            print('sair') 