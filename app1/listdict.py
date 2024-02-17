listStd=[
        {
            'Name':'Mr. Shakhawat',
            'age':22,
            'ID':170220240011
        },
        {
            'Name':'Mr. Rahim',
            'age':34,
            'ID':170220240012
        },
        {
            'Name':'Mr. Karim',
            'age':21,
            'ID':170220240013
        },
    ]
    
total_age=0
std_no=len(listStd)

for x in listStd:
    total_age=total_age+x['age']
avg_age1=total_age/std_no
print(avg_age1)

tage=0
stdno=len(listStd)
for student in listStd:
    for a,b in student.items():
        # print(a,b)
        if a=='age':
            tage+=b
print(tage/stdno)
