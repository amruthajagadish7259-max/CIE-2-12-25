from student import student_details
def test_student_details():
    expected_output=(
        "Student ID:01FE24BCA007\n"
        "Student Name:Tanvi\n"
        "Course Enrolled:DevOps\n"
        "Academic Year:2024"
    )
    assert student_details("01FE24BCA007","Tanvi","DevOps",2024)==expected_output
