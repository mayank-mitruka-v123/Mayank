'''
5.A bakery sells loaves of bread for 185 rupees each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old bread being
purchased from the user. Then your program should display the regular price for the bread,
the discount because it is a day old, and the total price. All of the values should be displayed
using two decimal places, and the decimal points in all of the numbers should be aligned
when reasonable values are entered by the user.
'''
n=float(input("Enter no. of loaves of new breads : "))
old=float(input("Enter no. of loaves of old breads : "))
rp=float(input("Enter regular price of the bread : "))
np=n*185
op=old*185
dp=op*(60/100)
print("Regular price : Rs.",rp)
print("Amount of new loaves: Rs.",np)
print("Amount of old loaves: Rs.",dp)
print("Total amount: Rs.",np+dp)
