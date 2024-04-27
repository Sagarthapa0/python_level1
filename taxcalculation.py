# sourcery skip: remove-redundant-if
'''
WAP  to accept the cost price of bike and display the road tax to be paid according to the following criteria
cost price(in rs)      tax
>100000               15%
>50000 and <=100000    10%
<=50000                5%

'''
cost_price =int(input("Enter your cost price: "))
if cost_price>100000:
    print("your road tax is 15%")
elif cost_price>50000 and cost_price<=100000:
    print("your road tax is 10%")
elif cost_price<=50000:
    print("your road tax is 5%")
else:
    print("not valid")