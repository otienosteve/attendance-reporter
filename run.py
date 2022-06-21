import csv
studentlist=["brian.cheruiyot01@student.moringaschool.com","wayne.musungu@student.moringaschool.com","edah.chepngetich@student.moringaschool.com","oscar.okolla@student.moringaschool.com","james.musembi@student.moringaschool.com","janeffer.njeri@student.moringaschool.com","hussein.salim@student.moringaschool.com","mary.auma@student.moringaschool.com","valarie.chelagat@student.moringaschool.com","david.kahumbi@student.moringaschool.com","ludwig.murimi@student.moringaschool.com","oliver.maiyo@student.moringaschool.com","mercy.mambui@student.moringaschool.com","julia.mwangi@student.moringaschool.com","oscar.kamau@student.moringaschool.com","sammy.muchiri@student.moringaschool.com","brian.laboso@student.moringaschool.com","victor.makori@student.moringaschool.com","nimrod.chitayi@student.moringaschool.com","paivy.eshirera@student.moringaschool.com","andre.kaeulana@student.moringaschool.com","lucy.mongwe@student.moringaschool.com","april.wairimu@student.moringaschool.com","clinton.wambugu@student.moringaschool.com","martin.misigo@student.moringaschool.com","marvin.kithinji@student.moringaschool.com","haimana.uta@student.moringaschool.com","shalyne.waweru@student.moringaschool.com","grace.nyutu@student.moringaschool.com","hussein.omar@student.moringaschool.com","ali.ali@student.moringaschool.com","george.gichuru@student.moringaschool.com"]
time=input("Is the CSV for the Morning or Evening Session? Reply with (m/e) ")
#Parse CSV file
present=[]
with open("attendance.csv") as attend:
    csv_data=csv.reader(attend)
    
    for data in csv_data:
        present.append(data[2])

#Remove unnecessary fields
present.remove('Email')
present.remove('steve.otieno@moringaschool.com')

#Check for absent students
absentstudents=[]
totalabsent=0
totalpresent=0
for std in studentlist:
    if std not in present:
        absentstudents.append(std)
        totalabsent+=1
    else:
        totalpresent+=1

with open('absentreport.txt','+a') as absent:
    if time=='m'.lower():
        absent.write("Absent for Morning Standup"+'\n')
    else:
        absent.write("Absent for Evening Synch"+'\n')
    for i in absentstudents:
      
        absent.write(i+'\n')

#Check for aliens in your class
fn=0
foreignemails=[]
for ptrs in present:
    if ptrs not in studentlist:
        foreignemails.append(ptrs)
        fn+=1
#Print report   
print(str(totalpresent)+' student(s) present ')
print(str(totalabsent)+" student(s) absent ")
for absentee in absentstudents:
    print(absentee)
if fn:
    print(" There seemed to have been "+str(fn)+" alien(s) in your class" )
    for alien in foreignemails:
        print(alien)
