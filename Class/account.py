class Account:
    def __init__(self, acc_no, pas):
        self.acc_no= acc_no
        self.pas=pas

acc1= Account("12345","abcde")
print(acc1.acc_no)
print(acc1.pas)