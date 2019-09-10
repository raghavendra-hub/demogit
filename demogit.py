students=0
teachers=0
for i in range(int(input())):
    t = input()
    temp1 = t.find("@student.college.edu")
    temp2 = t.find("@professor.college.edu")
    if(temp1!=-1):
        students=students+1
    elif(temp2!=-1):
        teachers=teachers+1
    else:
        pass

print(students,teachers)