from student import student_details
def test_student_details():
    expected_output=(
        "Student ID:01FE24BCA051\n"
        "Student Name:Deepa\n"
        "Course Enrolled:DevOps\n"
        "Academic Year:2024"
    )
    assert student_details("01FE24BCA051","Deepa","DevOps",2024)==expected_output
