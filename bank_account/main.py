from datetime import datetime

menu = """
# 
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
# 
"""
WITHDRAW_LIMIT = 3
WITHDRAW_AMOUNT_LIMIT = 500
number_withdrawals = 0
balance = 0.0
transaction_history = ()


def create_transaction(transaction_type, value):
    history = ()
    
    if transaction_type not in ["d", "w"]:
        raise ValueError("Transaction type must be [d]eposit or [w]ithdrawal")
    
    transaction_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    history += ((transaction_type, value, transaction_time),)
    return history


# def deposit(value):
#     create_transaction("d", value)
#     balance += value
#     return balance
    
# def withdraw(value):
#     global balance

#     create_transaction("w", value)
#     balance -= value
"""
Depositos: 
    - mostrar na operação extrato
Saque:
    - 3 saques diários, R$500 por saque. 
    - Saldo atual ao fim do extrato: R$xxx.xx
Extrato: 
    - Exibir depositos
    - Exibir saques
    - Exibir total da conta
"""

# while True:
    # user_input = input(menu)

    # match user_input:
        # case 'd': 
        #     amount = float(input("Amount: "))
        #     deposit(amount)
            
        # case 'w':
        #     amount = input("Amount: ")
        #     withdrawal(amount) 
            
        # case 'e':
        #     print('extrato') ls
        
        # case 'q':
        #     print('sair') 