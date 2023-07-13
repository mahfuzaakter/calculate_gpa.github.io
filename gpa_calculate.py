#total_subject= ["bangla","english","math","science"]
#marks = 100



bangla =float( input("Enter your bangla marks: "))

english =float( input("Enter your english marks: "))

math = float(input("Enter your math marks: "))

science =float(input("Enter your science marks: "))

avg_marks = (bangla + english + math + science)/4


def gpa(avg_marks):
 
 if avg_marks>=91 and avg_marks<=100:
  
  return "A+"
 elif avg_marks>=81 and avg_marks<=90:
  return "A"
 elif avg_marks>=71 and avg_marks<=80:
  return "B"
 elif avg_marks>=61 and avg_marks<=70:
  return "C"
 elif avg_marks>=41 and avg_marks<=60:
  return "D"
 
 else:
  return "F" 

gpa = gpa(avg_marks)


print("Average Marks:", avg_marks)
print("GPA:", gpa)