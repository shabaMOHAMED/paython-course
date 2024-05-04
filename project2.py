
str_length=input("please type Length : \n")
str_width=input("please type width : \n")
str_price=input("How much for 1 meter? \n")

#convert type
length=float(str_length)
width=float(str_width)
price=float(str_price)

total_area=length*width
total_price=total_area*price

area=str(total_area)
str_total_price=str(total_price)

print("The total erea is "+area)
print("Give The guy "+str_total_price+" $")