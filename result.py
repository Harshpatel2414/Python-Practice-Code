a= int(input("Enter your maths marks : "))
b= int(input("Enter your science marks : "))
c= int(input("Enter your english marks : "))


if(a<33 or b<33 or c<33):
    print("Fail! you have less marks in one or more subjects")

elif(a+b+c)/3 < 40:
    print("Fail! You have less percentage than 40")    

else:
    print("Congratulations! You are pass")