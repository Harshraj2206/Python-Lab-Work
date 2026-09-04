student_info = {
    "name": "Harsh Raj",
    "age": 21,
    "Branch": "CSE AIML"
}

# 1. Access a value
print(student_info["name"])

# 2. get() - safely get a value
print(student_info.get("age"))

# 3. keys() - get all keys
print(student_info.keys())

# 4. values() - get all values
print(student_info.values())

# 5. items() - get key-value pairs
print(student_info.items())

# 6. Add a new key-value pair
student_info["college"] = "ABC College"

# 7. Update an existing value
student_info["age"] = 22

# 8. update() - add/update multiple values
student_info.update({
    "city": "Patna",
    "age": 21
})

# 9. Check if a key exists
if "name" in student_info:
    print("Name exists")

# 10. pop() - remove a specific key
student_info.pop("city")

# 11. popitem() - remove the last key-value pair
student_info.popitem()

# 12. setdefault() - add key if it doesn't exist
student_info.setdefault("semester", 6)

# 13. copy() - create a copy
student_copy = student_info.copy()

# 14. len() - number of key-value pairs
print(len(student_info))

# 15. Loop through dictionary
for key, value in student_info.items():
    print(key, ":", value)

# 16. clear() - remove everything
student_info.clear()

print(student_info)






