frnd_bdates = {'Tanu':'12 june','Vidya':'26dec','Theju':'8oct'}
print(frnd_bdates)
name = input('Enter the name to be searched :')
if name in frnd_bdates.keys():
    print(name + '  bdate is  ' +frnd_bdates[name])
else:
    print('Name not present,Enter bdate')
    frnd_bdates[name] = input()
print(frnd_bdates)
