m=input("Enter the month : ")
d=int(input("Enter date : "))
if m in ('December','January','February','March'):
    if m=='March' and d<20:
        print('The season is currently Winter')
    elif m=='March' and d>20:
        print('The season is currently summer')
    else:
        print("The season is currently Winter")
elif m in ("April","May","June"):
    if m=='June' and d<21:
        print("The season is currently Summer.")
    elif m=='June' and d>21:
        print("The season is currently Spring")
elif m in("July",'August','September'):
    if m=="September" and d<22:
        print("The season is currently Spring.")
    elif m=="September" and d>22:
        print("The season is currently Fall")
