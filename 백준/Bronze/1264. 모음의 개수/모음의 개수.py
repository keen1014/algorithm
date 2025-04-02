arr =[]
while True:
    r = input()
    arr.append(r)
    if   '#' in r:
        break
for i in range(len(arr)-1):
    print(arr[i].count('a')+arr[i].count('e')+arr[i].count('i')+arr[i].count('o')+arr[i].count('u')+arr[i].count('A')+arr[i].count('E')+arr[i].count('I')+arr[i].count('O')+arr[i].count('U'))