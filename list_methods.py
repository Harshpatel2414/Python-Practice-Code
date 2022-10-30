list = ["harsh", "yash" , "shriram", "ashwin", "bhavesh"]
print(list)
#list methods

l1 =[12, 24, 45, 21, 11, 5, 56]
# 1. append()
l1.append(90)
print(l1)

# 2. sort() 
l1.sort()
print("sorted list ",l1)

# 3. reverse()
l1.reverse()
print("reverse list ",l1)

# 4. pop()
l1.pop() #delete last element default
print(l1)

# 5. insert()
l1.insert(1,345)
print(l1)

# 6. remove()
l1.remove(345)
print(l1)

# 6. slicing
print(l1[0:3])