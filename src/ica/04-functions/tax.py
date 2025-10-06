def add_tax(price,tax_rate):
    tax_amt=price*tax_rate
    return price+tax_amt

p = int(input("Please enter price"))
t_rate = float(input("Please enter tax rate"))
print(add_tax(p,t_rate))