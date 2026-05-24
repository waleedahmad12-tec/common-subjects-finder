print("=" * 40)
print("      COMMON SUBJECTS FINDER")
print("=" * 40)

student1 = {"Math", "Physics", "English", "Computer"}
student2 = {"Physics", "Chemistry", "English", "Biology"}

common_subjects = student1.intersection(student2)
all_subjects = student1.union(student2)

print("\nSubjects of Student 1:")
print(student1)

print("\nSubjects of Student 2:")
print(student2)

print("\nCommon Subjects:")
print(common_subjects)

print("\nAll Subjects:")
print(all_subjects)

print("\nTotal Common Subjects:", len(common_subjects))

print("\n" + "=" * 40)
print("        PROJECT COMPLETED")
print("=" * 40)
