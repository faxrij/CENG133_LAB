students = int(input('Number of students: '))
grade_list = []
for i in range(students):
  midterm1 = int(input('midterm1: '))
  midterm2 = int(input('midterm2: '))
  final = int(input('final : '))
  result = midterm1*0.3+midterm2*0.3+final*0.4
  grade_list.append([midterm1,midterm2,final,result])
print(grade_list)