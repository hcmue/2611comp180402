# Mở và tự đóng file dùng with
# Tính tổng số giờ và trung bình giờ làm mỗi ngày
import json
emps = []
with open("hours.txt", encoding="utf8") as myfile:
    for line in myfile:
        tmp = line.split() # Phân tách theo khoảng trắng
        emp_timesheet = [float(item) for item in tmp[2:]]
        emp = {
            "manv": tmp[0],
            "tennv": tmp[1],
            "time_sheet": emp_timesheet,
            "total": sum(emp_timesheet),
            "avg": sum(emp_timesheet) / len(emp_timesheet)
        }
        print(emp)
        emps.append(emp)
with open("output.json", "w", encoding="utf8") as f:
    json.dump(emps, f)