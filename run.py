import csv
studentlist=["brian.cheruiyot01@student.moringaschool.com","wayne.musungu@student.moringaschool.com","edah.chepngetich@student.moringaschool.com","oscar.okolla@student.moringaschool.com","james.musembi@student.moringaschool.com","janeffer.njeri@student.moringaschool.com","hussein.salim@student.moringaschool.com","mary.auma@student.moringaschool.com","valarie.chelagat@student.moringaschool.com","david.kahumbi@student.moringaschool.com","ludwig.murimi@student.moringaschool.com","oliver.maiyo@student.moringaschool.com","mercy.mambui@student.moringaschool.com","julia.mwangi@student.moringaschool.com","oscar.kamau@student.moringaschool.com","sammy.muchiri@student.moringaschool.com","brian.laboso@student.moringaschool.com","victor.makori@student.moringaschool.com","nimrod.chitayi@student.moringaschool.com","paivy.eshirera@student.moringaschool.com","andre.kaeulana@student.moringaschool.com","lucy.mongwe@student.moringaschool.com","april.wairimu@student.moringaschool.com","clinton.wambugu@student.moringaschool.com","martin.misigo@student.moringaschool.com","marvin.kithinji@student.moringaschool.com","haimana.uta@student.moringaschool.com","shalyne.waweru@student.moringaschool.com","grace.nyutu@student.moringaschool.com","hussein.omar@student.moringaschool.com","ali.ali@student.moringaschool.com","george.gichuru@student.moringaschool.com"]

# parse CSV file
present=[]
with open("attendance.csv") as attend:
    csv_data=csv.reader(attend)
    
    for data in csv_data:
        present.append(data[2])

#Remove unnecessary fields
present.remove('Email')
present.remove('steve.otieno@moringaschool.com')

# Check for absent students
absents=' '
totalabs=0
prst=0
for std in studentlist:
    if std not in present:
        absents+=std+' '
        totalabs+=1
    else:
        prst+=1
        

# check for aliens in your class

fn=0
foreignemails=''
for ptrs in present:
    if ptrs not in studentlist:
        foreignemails+=ptrs
        fn+=1
   
print(str(prst)+' students were present '+str(totalabs)+" were/was absent [ "+absents+" ] there were "+str(fn))
if fn:
    print(" There seemed to have been "+str(fn)+" alien(s) in your class [ "+foreignemails+" ]" )
