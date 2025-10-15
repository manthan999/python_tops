person = {
    "name": "manthan",
    "age": 20,
    "city": "surat",
    "profession": "Engineer"
}

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Profession:", person["profession"])

print("Country:", person.get("country", "Not specified"))  
