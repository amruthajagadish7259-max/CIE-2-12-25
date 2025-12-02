from student import student_details
def test_student_details():
    expected_output=(
        "Student ID:01FE24BCA011\n"
        "Student Name:Amrutha\n"
        "Course Enrolled:DevOps\n"
        "Academic Year:2025"
    )
    assert student_details("01FE24BCA011","Amrutha","DevOps",2024)==expected_output
