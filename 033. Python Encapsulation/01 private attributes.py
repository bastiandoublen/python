class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.__balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      print(f"Deposited {amount}. New balance: {self.__balance}")

  def get_balance(self):
    return self.__balance

account = BankAccount("Alice", 1000)
print(account.owner)
print("Balance:", account.get_balance())
account.deposit(500)
