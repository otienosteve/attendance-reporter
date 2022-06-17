import csv
studentlist=[]
present=[]
with open("attendance.csv") as attend:
    csv_data=csv.reader(attend)
    
    for data in csv_data:
        present.append(data[2])

present.remove('Email')
present.remove('steve.otieno@moringaschool.com')
totalprst=len(present)
print(str(len(present))+' total students were present')
