class Sale:
    def __init__(self,town,product,price,quantity):
        self.town = town
        self.product=product
        self.price=price
        self.quantity=quantity

def read_sale():
    inputDate = input().split(' ')
    town = inputDate[0]
    product = inputDate[1]
    price = float(inputDate[2])
    quantity = float(inputDate[3])
    currentSale = Sale(town,product,price,quantity)
    return currentSale

towns = set()
sales = list()
numberOfSales = int(input())
for sale in range(0,numberOfSales):
    sale = read_sale()
    sales.append(sale)
    towns.add(sale.town)

townsBySales = dict()

for currentTown in towns:
    townsBySales.setdefault(currentTown,0)
    for sale in sales:
        if sale.town == currentTown:
            townsBySales[currentTown]+=sale.quantity*sale.price

print(townsBySales)
