from student import Student 
FILENAME = "data.txt" 
def save_student(student): 
with open(FILENAME, "a") as file: 
file.write(student.to_file_format()) 
def load_students(): 
students = [] 
try: 
with open(FILENAME, "r") as file: 
for line in file: 
name, age, student_id, course = line.strip().split(",") 
student = Student(name, int(age), student_id, course) 
students.append(student) 
except FileNotFoundError: 
# File does not exist yet 
pass 
return students