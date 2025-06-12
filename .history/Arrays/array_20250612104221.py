arr = [1,2,3]

arr.append(4)
print(arr)

arr.insert(2,5)
arr.append(6)
print(arr)

print()

arr.pop()
print(arr)
print()

arr.remove(5)
print(arr)

print()
print(arr[3])

print()

for x in arr:
    print(x)

for x in range(len(arr)):
    print("new value: ", arr[x])


#so for inserting into an array or list
#arrayname.insert(last position value, new value)
#for addinf
#arrayname.append(new value)

##deleting in array
#arrayname.pop() removes the last elemnt
#arrayname.remove(value) emoves the exact value

"""
for accesing in arra or list
print(arryname[index position])
"""

print(arr)
print()

print(arr[-1])