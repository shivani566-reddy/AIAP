class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += float(amount)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= float(amount)

    def get_balance(self) -> float:
        return self._balance
if __name__ == "__main__":
    # simple demo
    acct = BankAccount(100)
    acct.deposit(50)
    try:
        acct.withdraw(30)
    except ValueError as e:
        print(e)
    print(f"Balance: {acct.get_balance():.2f}")


