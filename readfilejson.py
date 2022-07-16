import json

dat = open('Jsondata.json')
print(dat.read())
print("Type:", type(dat))

with open('Jsondata.json') as data:
    Datajson = json.load(data)
    #print(Datajson)
    DataPerple = Datajson['Perplejson']
    for jsonfile in DataPerple:
        print('Name: ' + jsonfile['name'],end = " ")
        print('Lastname: ' + jsonfile['lastname'])
        print('Age: ' + jsonfile['age'])
        print('Pred: ' + jsonfile['pred'] + ' %')