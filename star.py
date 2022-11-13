'''
#star pattern like this
	      *
    	**
  	***
	****
'''
n = int(input("Enter the number : "))
for i in range(n):
	print(" "*(n-i),end="")
	print("*"*(i+1))
