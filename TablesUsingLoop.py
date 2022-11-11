a = int(input("Enter the number : "))
print("Table of", a, "is :")
for i in range(1,11):
	 #print(str(a)+" X " +str(i)+" = " + str(i*a))
	 print(f"{a} X {i} = {i*a}") #using f-string
	 