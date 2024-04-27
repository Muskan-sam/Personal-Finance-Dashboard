class Income:
    def __init__(self, source, amount):
      self.source = source
      self.amount = amount
      

    def __repr__(self):
      return f"<Income: {self.source}, ${self.amount:.2f}>"
