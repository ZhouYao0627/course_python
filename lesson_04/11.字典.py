d = {
    'name': '孙悟空',
    'age': '18',
    'gender': '男',
    'name': 'suwukong'
}

# print(d)

# print(d['name'],d['age'],d['gender'])

# print(d.keys())

# print(d['name'])

for k in d.keys():
    print(k,d[k])
print('*'*20)
for v in d.values():
    print(v)
print('*' * 20)
for k,v in d.items():
    print(k,v)

