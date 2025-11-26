strings = [
    "Hello, world!",
    "Python is fun.",
    "Writing multiple strings into a file.",
    "End of file."
]

with open("output.txt", "w") as file:
    for s in strings:
        file.write(s + "\n")  

print("Strings have been written to output.txt")
