# Nested Lists

# A dataset representing students' scores in different subjects
students_scores = [
    ["Alice", [85, 90, 78]],  # Name and scores
    ["Bob", [88, 76, 92]],
    ["Charlie", [92, 85, 89]]
]

# Accessing data [row][collumn]
print(students_scores[0][0])  # Output: "Alice" (first student's name)
print(students_scores[1][1])  # Output: [88, 76, 92] (Bob's scores)
print(students_scores[2][1][0])  # Output: 92 (Charlie's first score)

# Looping through data
for student in students_scores:
    name = student[0]
    scores = student[1]
    print(f"{name}'s scores: {scores}")





# Nested Dictionaries 

# A dataset representing students and their scores in specific subjects
students_scores = {
    "Alice": {"Math": 85, "English": 90, "Science": 78},
    "Bob": {"Math": 88, "English": 76, "Science": 92},
    "Charlie": {"Math": 92, "English": 85, "Science": 89}
}

# Accessing data
print(students_scores["Alice"])  # Output: {"Math": 85, "English": 90, "Science": 78}
print(students_scores["Bob"]["Math"])  # Output: 88 (Bob's Math score)

# Looping through data
for student, subjects in students_scores.items():
    print(f"{student}'s scores:")
    for subject, score in subjects.items():
        print(f"  {subject}: {score}")





# Combination of Both

# A dataset of students with multiple test scores in various subjects
students_data = [
    {"name": "Alice", "scores": {"Math": [85, 88], "English": [90, 92]}},
    {"name": "Bob", "scores": {"Math": [78, 82], "English": [76, 80]}},
]

# Accessing data
print(students_data[0]["name"])  # Output: "Alice"
print(students_data[1]["scores"]["English"])  # Output: [76, 80]

# Looping through data
for student in students_data:
    print(f"{student['name']}'s scores:")
    for subject, scores in student["scores"].items():
        print(f"  {subject}: {scores}")

