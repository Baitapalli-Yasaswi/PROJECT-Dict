# Creating dictionaries:
Student_details ={
    "Name":"M.Rohini",
    "Gr.No":224513,
    "ENroll NO.":92600114456,
    "College":"Marwadi University",
    "Branch":"CSE AI/ML"
}
# Accessing Lists:
#print(Student_details["Name"])
#print(Student_details["ENroll NO."])
#print(Student_details["Branch"]) 

# Adding Elements:
Student_details["City"] = "Kakinada"
#print(Student_details)
Student_details["ph.no"] = 7896321561
#print(Student_details) 

# Dictionary Methods:
#print(Student_details.keys())
#print("-----------------------------------")
#print(Student_details.values())
#print("-----------------------------------")
#print(Student_details.items())
#print("-----------------------------------")
#print(Student_details.get("Name"))
#print("--------------------------------------")
#print(Student_details.get("Branch"))
#print("-----------------------------------")
#print(Student_details.get("Gr.No"))
#print("-----------------------------------")
#Student_details.pop("ph.no")
#print(Student_details)
#print("-----------------------------------")
#Student_details.update([("Gr.No",224512)])
#print(Student_details) 

# Dictionary Loops: 
for key in Student_details:
    print(key)
    print("---------------------------------------")
print("==================================================")
for value in Student_details.values():
    print(value)    
    print("---------------------------------------")
print("============================================================")
for key,value in Student_details.items():
    print(f"{key}:{value}")


