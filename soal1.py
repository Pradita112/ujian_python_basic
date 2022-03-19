data = []

dc1 = {
    'nama' : 'budi',
    'umur': '18',
    'gender': 'laki-laki',
}
dc2 = {
    'nama' : 'rani',
    'umur': '20',
    'gender': 'perempuan',
}
dc3 = {
    'nama' : 'yani',
    'umur': '19',
    'gender': 'perempuan',
}
dc4 = {
    'nama' : 'robi',
    'umur': '17',
    'gender': 'laki-laki',
}
dc5 = {
    'nama' : 'fani',
    'umur': '22',
    'gender': 'laki-laki',
}
data.append(dc1)
data.append(dc2)
data.append(dc3)
data.append(dc4)
data.append(dc5)
count = 0
#print(data)
for i in data:
    if i['gender'] == 'laki-laki':
        print('hai')
        count += 1
print(count)
   


        


