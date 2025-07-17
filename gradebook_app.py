num_subjects = int(input("Enter the number of subjects: "))

marks_list = []
for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks_list.append(mark)

total_marks = sum(marks_list)
avrg_marks = total_marks / num_subjects

if avrg_marks >= 80:
    grade = "A+"
elif avrg_marks >= 70:
    grade = "A"
elif avrg_marks >= 60:
    grade = "A-"
elif avrg_marks >= 50:
    grade = "B"
elif avrg_marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {avrg_marks}")
print(f"Grade: {grade}")

print("\n--- Gradebook Summary ---")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {avrg_marks:.2f}")
print(f"Grade: {grade}")