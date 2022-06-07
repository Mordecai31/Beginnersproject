from datetime import datetime

product = {'DELL': 100000, "HP": 2200000, 'LENOVO': 3300000, 'ACER': 4400000, 'OTHER': 3300000}

print("Welcome to Online Store")

a = input("Enter the Product Name:").upper().replace(" ", "")

def PrintPriceDetail(productName, price, discount):
    print(f"Your have Purchased {productName} Laptop at a Price of N{price} and the Discount applied was {discount} on {datetime.now().time()}")

def calculateproduct(a):
  if a == "HP":
    price = product[a] - 0.15 * product[a]
    PrintPriceDetail(a, price, "15%")

  elif a == 'DELL':
      price = product[a] - 0.1 * product[a]
      PrintPriceDetail(a, price, "10%")

  elif a == 'LENOVO':
     price = product[a] - 0.005 * product[a]
     PrintPriceDetail(a, price, "5%")

  elif a == 'ACER':
     price = product[a] - 0.25 * product[a]
     PrintPriceDetail(a, price, "25%")

  else:
     b = 'OTHER'
     price = product[b] - 0.01 * product[b]
     PrintPriceDetail(b, price, "1%")


calculateproduct(a)
