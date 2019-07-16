import copy

a = [[1,2,3] , [4,5,6]]
b = a
print(" a and b before modify ")
print(a)
print(b)
a[0][1] = 10
print ( "a and b after modify . b was obtained as a deep copy og a")
print(a)
print(b) #aici  se modifica si b ul

b = copy .deepcopy(a)
print("a and b before modification");
print(a)
print(b)

a[0][1]=9
print("after")
print(a)
print(b) #aici ramane b ul nemodificat
