# Dictionary in the python
# syntax of dictionary dic ={}

dic = {"name":"harsh", "roll":15, "rank":1,"address":"nandurbar"}
print(dic)

# Dictionary methods

# 01. key()
print(dic.keys()) 
print(list(dic.keys())) #In the list formate

# 02. values()
print(dic.values())

# 03. update()
dic.update({"name":"yash"})
print(dic)

# 04. items()
print(dic.items())

# 05. clear()
print(dic.clear()) #delete the dictionary



