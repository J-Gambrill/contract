company_data = {                                                                                      #dictionary
    "departments": [                                                                                    #list
        {                                                                                                 #dictionary
            "name": "Engineering",
            "employees": [                                                                                   #list 
                {                                                                                              #dictionary
                    "id": 101,
                    "name": "Alice",
                    "age": 29,
                    "skills": ["Python", "JavaScript", "SQL"],
                    "projects": [
                        {"project_id": "P1", "name": "Inventory App", "status": "Completed"},
                        {"project_id": "P3", "name": "Data Pipeline", "status": "Ongoing"}
                    ]
                },
                {
                    "id": 102,
                    "name": "Bob",
                    "age": 35,
                    "skills": ["Java", "AWS", "Docker"],
                    "projects": [
                        {"project_id": "P2", "name": "Cloud Migration", "status": "Ongoing"}
                    ]
                }
            ]
        },
        {
            "name": "Marketing",
            "employees": [
                {
                    "id": 201,
                    "name": "Charlie",
                    "age": 40,
                    "skills": ["SEO", "Content Writing", "Analytics"],
                    "projects": [
                        {"project_id": "P4", "name": "Brand Campaign", "status": "Completed"}
                    ]
                }
            ]
        }
    ]
}


# Task: Find and manipulate the data

# output data

# print(company_data[1]["name"]) will result in error as it is a dictionary which means you need to go through a key ["..."]
print(company_data["departments"][0]["name"])  # prints engineering
print(company_data["departments"][0]["employees"])  # prints all data in employees

#lets get more specific

# marketing project status

print(company_data["departments"][1]["employees"][0]["projects"][0]["status"])

# the name of employee 102 "bob" 

print(company_data["departments"][0]["employees"][1]["name"])

# add some data to bobs skills   dept = department  emp = employee
#this is where it gets confusing as supposedly i have to convert the list to a set and back.

for dept in company_data["departments"]:
    for emp in dept['employees']:
        if emp["name"] == 'Bob':
            emp["skills"] = list(set(emp['skills'])) 
            emp['skills'].append('swimming')
            print(f"Updated skills for {emp['name']}: {emp['skills']}")

# turning it into a set means duplicates wont be added