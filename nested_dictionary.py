student_info = {
        "student1": {
            "name": "Harsh Raj",
            "age": 21,
            "branch": "CSE AIML",
            "subjects": ["Maths", "Physics", "Chemistry"],
            "marks": {
                "Maths": 95,
                "Physics": 90,
                "Chemistry": 85
            }   
        },

        "student2": {
            "name": "Kavya Patel",
            "age": 20,
            "branch": "CSE DS",
            "subjects": ["Maths", "Biology", "English"],
            "marks": {
                "Maths": 88,
                "Biology": 92,
                "English": 80
        }
    }
}
# Acessing the info for student1
print(student_info["student1"]["name"])
print(student_info["student1"]["age"])
print(student_info["student1"]["branch"])

print("Subjects for student1:", student_info["student1"]["subjects"])
print("Marks for student1:", student_info["student1"]["marks"])

print("Maths marks for student1:", student_info["student1"]["marks"]["Maths"])
print("Physics marks for student1:", student_info["student1"]["marks"]["Physics"])
print("Chemistry marks for student1:", student_info["student1"]["marks"]["Chemistry"])

print(student_info["student1"]["subjects"][0])  # Accessing the first subject of student1


# Acessing the info for student2
print(student_info["student2"]["name"])
print(student_info["student2"]["age"])  
print(student_info["student2"]["branch"])

print("Subjects for student2:", student_info["student2"]["subjects"])
print("Marks for student2:", student_info["student2"]["marks"])

print("Maths marks for student2:", student_info["student2"]["marks"]["Maths"])
print("Biology marks for student2:", student_info["student2"]["marks"]["Biology"])
print("English marks for student2:", student_info["student2"]["marks"]["English"])

print(student_info["student2"]["subjects"][0])  # Accessing the first subject of student2

