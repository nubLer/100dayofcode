student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for name,score in student_scores.items():
    
    if score > 91:
        grade = "Outstanding"
    elif score <= 90 and score >= 81:
        grade = "Exceeds Expectations"
    elif score <= 80 and score >= 71:
        grade = "Acceptable"
    elif score <= 70:
        grade = "Fail"
    student_grades[name] = grade
print(student_grades)