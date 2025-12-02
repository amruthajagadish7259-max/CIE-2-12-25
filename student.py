def student_details(s_id,s_name,course,academic_year):
   result=(
      f"Student ID:{s_id}\n"
      f"Student Name:{s_name}\n"
      f"Course Enrolled:{course}\n"
      f"Academic Year:{academic_year}"
   )
   return result
   
if __name__=="__main__":
      s_id="01FF24BCA055"
      s_name="Pratibha"
      course="DevOps"
      academic_year=2024
      print(student_details(s_id,s_name,course,academic_year))
