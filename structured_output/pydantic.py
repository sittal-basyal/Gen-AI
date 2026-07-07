from pydantic import Basemodel , EmailStr , Field
from typinf import Optional
class Student(Basemodel):
    name:str = "Sittal"
    age:Optional[int] = None 
    grade:float = Field(gt = 0, lt = 10, description = "Grade must be between 0 and 10" , default = 0)
    email:EmailStr
    is_active:bool

new_student ={'name': "Sittal", 'age': 20, 'grade': 8.5, 'email': "sitall@example.com" }
student = Student(**new_student)

student_dict = student.model_dump()

print(student_dict)

student_json = student.model_dump_json()
print(student_json)