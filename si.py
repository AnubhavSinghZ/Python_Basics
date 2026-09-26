# __SIMPLE CALCULATOR__

def calculate_si():
    print("==SIMPLE INTEREST CALCULATOR==")

    p=float(input("Enter Principle Ammount(P):"))
    r=float(input("Enter Rate Of Interest(R):"))
    t=float(input("Enter Time in Years (T):"))

    #Formula: SI=(P*R*T)/100
    si=(p*r*t)/100
    total_amount=p+si

    print("-"*30)
    print(f"Simple Interest:{si}")
    print(f"Total Payable Amount:{total_amount}")
    print("-"*30)
# calling the function

calculate_si()    