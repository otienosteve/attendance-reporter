import csv
studentlist=["brian.cheruiyot01@student.moringaschool.com","wayne.musungu@student.moringaschool.com","edah.chepngetich@student.moringaschool.com","oscar.okolla@student.moringaschool.com","james.musembi@student.moringaschool.com",
"janeffer.njeri@student.moringaschool.com","hussein.salim@student.moringaschool.com","mary.auma@student.moringaschool.com","valarie.chelagat@student.moringaschool.com","david.kahumbi@student.moringaschool.com","ludwig.murimi@student.moringaschool.com",
"oliver.maiyo@student.moringaschool.com","mercy.mambui@student.moringaschool.com","julia.mwangi@student.moringaschool.com","oscar.kamau@student.moringaschool.com","sammy.muchiri@student.moringaschool.com","brian.laboso@student.moringaschool.com","victor.makori@student.moringaschool.com","nimrod.chitayi@student.moringaschool.com","paivy.eshirera@student.moringaschool.com","andre.kaeulana@student.moringaschool.com","lucy.mongwe@student.moringaschool.com",
"april.wairimu@student.moringaschool.com","martin.misigo@student.moringaschool.com","marvin.kithinji@student.moringaschool.com","haimana.uta@student.moringaschool.com",
"shalyne.waweru@student.moringaschool.com","grace.nyutu@student.moringaschool.com","hussein.omar@student.moringaschool.com","george.gichuru@student.moringaschool.com","ali.ali@student.moringaschool.com","clinton.wambugu@student.moringaschool.com"
]
present=[]
with open("attendance.csv") as attend:
    csv_data=csv.reader(attend)
    
    for data in csv_data:
        present.append(data[2])



present.remove('Email')
present.remove('steve.otieno@moringaschool.com')
absentees=[]
for std in studentlist:
    if std not in present:
        absentees.append(std)
    if '***' in present:
        absentees.append(present.index["***"]+"<-verify")
absnt=""
for abs in absentees:
    absnt+=" "+abs

foreignemails=' '
fn=0
for prst in present:
    if '***' in prst:
        foreignemails+=prst+" "
        fn+=1
totalprst=len(present)
absent=len(studentlist)-totalprst
if absent ==0:
    print("All students were present, If you have doubts you can confirm")
else:
    print(str(totalprst)+' students were present '+str(absent)+" were absent namely "+absnt+" there were "+str(fn)+" student(s) who used foreign emails [ "+foreignemails+" ]")
