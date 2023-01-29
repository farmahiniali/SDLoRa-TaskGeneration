#-
with open("prime_mat_100-000.txt",'r') as f:
    file = f.read()
    arr = file.split(',')
    print("file of ",f.name," has length of : ",len(arr))

print('goodbye')