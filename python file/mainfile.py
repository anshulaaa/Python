from binaryconversion import binaryconversations
from binnaryadder import binaryadders
#from binnaryadder import decimltobinary
print(" Welcome to Binnary Adder ")
runs="yes"
while runs=="yes" or runs=="y":
    ins=False
    while ins==False:
        try:
            x=int(input("Enter the First number: "))
            if(x<0 or x>255):
                print("the number must be between 0 and 255")
            else:
                ins=True
        except:
            print("Please input a valid number")
    ins=False
    while ins==False:
        try:
            y=int(input("enter the second number:"))
            if (y<0 or y>255):
                print("the number must be between 0 and 255 ")  
            else:
                ins=True
        except:
              print("please input a valid number")
    print("The binary value of {} is:{}\n".format(x,binaryconversations(x)))
    print("The binary value of {} is:{}\n".format(y,binaryconversations(y)))
    a=binaryconversations(x)
    b=binaryconversations(y)
    sums1=binaryadders(str(a),str(b))
    print("The sum of {} and {} is:{}\n".format(x,y,sums1))
    runs=input("Do you want to continue? yes/no:")
    
