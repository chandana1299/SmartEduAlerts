from config import ATTENDANCE_THRESHOLD

def analyze_student(student):
    issues = []

    if student["attendance"] < ATTENDANCE_THRESHOLD:
        issues.append("low attendance")

    if student["fee"].lower() == "pending":
        issues.append("pending fees")

    return issues
