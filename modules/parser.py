import pandas as pd

def parse_file(file):
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    students = []
    for _, row in df.iterrows():
        students.append({
            "name": row["Name"],
            "attendance": row["Attendance"],
            "fee": row["Fee"],
            "chat_id": row["ChatID"]
        })
    return students
