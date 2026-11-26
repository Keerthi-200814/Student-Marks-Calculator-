maths = float(input("Enter Mathematics marks: "))
python = float(input("Enter Python marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + python + chemistry
average = total / 3

if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
else:
    grade = "C"

print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
