from datetime import datetime

menu = """

[d] Deposit 
[w] Withdraw
[s] Statement
[q] Quit

"""

WITHDRAW_LIMIT = 3
WITHDRAW_AMOUNT_LIMIT = 500
balance = 0.0
transaction_history = ()


def create_transaction(transaction_type, value):
    if transaction_type not in ["d", "w"]:
        raise ValueError("Transaction type must be [d]eposit or [w]ithdrawal")

    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return ((transaction_type, value, transaction_time),)


while True:
    user_input = input(menu)

    match user_input:
        case "d":
            try:
                amount = float(input("Amount: "))

                if amount < 0:
                    raise ValueError("Invalid amount")

                balance += amount
                transaction_history += create_transaction("d", amount)
                print("Transaction successful")

            except ValueError as e:
                print("Error:", e)

        case "w":
            try:
                amount = float(input("Amount: "))

                if amount <= 0:
                    raise ValueError("Invalid amount")

                if amount > 500:
                    raise ValueError("The withdrawal limit is R$500,00")

                if amount > balance:
                    raise ValueError("Insufficient funds")

                count_withdrawals = 0
                today = datetime.now().strftime("%Y-%m-%d")

                for type, _value, transaction_datetime in transaction_history:
                    if type == "w" and transaction_datetime.startswith(today):
                        count_withdrawals += 1

                if count_withdrawals >= WITHDRAW_LIMIT:
                    raise ValueError("Maximum daily withdrawals have been reached")

                balance -= amount
                transaction_history += create_transaction("w", amount)
                print("Transaction successful")

            except ValueError as e:
                print("Error:", e)

        case "s":
            for type, value, transaction_datetime in transaction_history:
                print(
                    f"Operation: {type}\nValue: R$ {value:.2f}\nDate: {transaction_datetime}"
                )
                print("----------------------")
            print(f"Total: R$ {balance:.2f}")

        case "q":
            print("Exiting program...")
            break

        case _:
            print("Invalid option")
