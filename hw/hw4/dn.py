file = open("IP.txt", "r")
z  = ''
for row in file:
    name = row.split()
    if str(row[1:]):
        print(row[0:14])
        print(z, row)


file.close()

file1 = open("DNS.txt", "r")
y = ''
for row1 in file1:
    name1 = row1.split()
    if str(row1[1:]):
        print(row1[0:14])
        print(y, row1)

file1.close()

file2 = open("host DNS.txt", "r")
x = ''
for row2 in file2:
    name2 = row2.split()
    if str(row2[1:]):
        print(row2[0:14])
        print(x, row2)

file2.close()


