class Savings:
  def __init__(self, savings_type, amount):
    self.savings_type = savings_type
    self.amount = amount
    

  def __repr__(self):
    return f"<Savings: {self.savings_type}, ${self.amount:.2f} >"
