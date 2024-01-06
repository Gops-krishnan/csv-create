import csv
with open("Employee.csv", "w") as f:
    w=csv.writer(f)
    w.writerow(["Eid", "Ename", "Company"])
    no=int(input("Enter the no of Employee"))
    for x in range(no):
        eid=int(input("Enter the Employee ID: "))
        ename=input("Enter the Employee Name: ")
        company=input("Enter the  Company Name: ")
        w.writerow([eid,ename,company])
