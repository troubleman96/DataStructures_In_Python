my_info = {
    "name": "trouble",
    "phone": "123456",
    "email": "itsabc@de.com"
}

student = dict(name="kelly", age="12")

#accesing dict values

print(my_info["email"])
print(student.get("age"))

##adding n updating on dict

my_info["email"] = "itssss@g.com"
student["course"] = "science"