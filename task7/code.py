n = int(input("Enter Number of Students: "))
m = int(input("Enter Number of Subjects: "))

if n <= 0 or m <= 0:
    print("Invalid Number of Students or Subjects")

else:
    students = []
    subjects = []
    marks = []


    for i in range(n):
        name = input("Enter Student Name: ")
        students.append(name)

   
    for j in range(m):
        subject = input("Enter Subject Name: ")
        subjects.append(subject)

    
    for i in range(n):
        row = []
        print("\nMarks for", students[i])

        for j in range(m):
            mark = float(input(subjects[j] + ": "))

            if mark < 0 or mark > 100:
                print("Invalid Marks! Enter 0 to 100.")
                row = []
                break

            row.append(mark)

        if len(row) != m:
            break

        marks.append(row)

    if len(marks) == n:

        # Student-wise analysis
        totals = []
        averages = []

        for i in range(n):
            total = sum(marks[i])
            average = total / m

            totals.append(total)
            averages.append(average)

       
        subject_totals = []
        subject_averages = []

        for j in range(m):
            total = 0

            for i in range(n):
                total += marks[i][j]

            average = total / n

            subject_totals.append(total)
            subject_averages.append(average)

        
        top_average = max(averages)

        print("\nEnter Minimum Subject Average Threshold:")
        threshold = float(input())

        print("\n========================================")
        print("       STUDENT PERFORMANCE REPORT")
        print("========================================")

        print("\nSTUDENT-WISE ANALYSIS")

        for i in range(n):
            print(students[i],
                  "Total:", totals[i],
                  "Average:", round(averages[i], 2))

        print("\nSUBJECT-WISE ANALYSIS")

        for j in range(m):
            print(subjects[j],
                  "Total:", subject_totals[j],
                  "Average:", round(subject_averages[j], 2))

        print("\nTOP PERFORMING STUDENT(S):")

        for i in range(n):
            if averages[i] == top_average:
                print(students[i])

        print("Highest Average:", round(top_average, 2))

        print("\nLOW-PERFORMING SUBJECTS:")

        found = False

        for j in range(m):
            if subject_averages[j] < threshold:
                print(subjects[j])
                found = True

        if not found:
            print("No Low-Performing Subjects")

        print("\n========================================")
        print("       ANALYSIS COMPLETED")
        print("========================================")

    else:
        print("Program stopped due to invalid marks.")

