class Launch:
    def __init__(self, year:int, month:int, succ:bool):
        self.year = year
        self.month = month
        self.succ = succ
    def __str__(self):


l = Launch(15,15,True)
print(l)