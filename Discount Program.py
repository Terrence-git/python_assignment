product_name=input("Enter your product name")
product_price=int(input("Enter the product price"))
if product_price>10000:
    discount=0.2
elif product_price>5000 and product_price <10000:
    discount=0.1
else:
    discount=0.0

discount_price=product_price-(discount*product_price)
print(f"{product_name} now costs {discount_price} after discount")