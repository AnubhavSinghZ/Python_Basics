class Account:
    def __init__(self, acc_no, acc_pas):
        self.acc_no= acc_no
        self.__acc_pas=acc_pas
    def reset_pass(self):
        print(self.__acc_pas)

acc1= Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())



class Person:
    __name="anonymous"  # conceptual private
    def __hello(self):
        print("hello person")
    def welcome(self):
        self.__hello()
p1= Person()

print(p1.welcome())
