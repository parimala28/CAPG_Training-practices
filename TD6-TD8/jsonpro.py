
import json

# Creating a dictionary
data = {"name": "John", "age": 30, "city": "New York"}

# Converting dictionary to JSON string
json_data = json.dumps(data)
print(f"JSON data: {json_data}")

# Parsing JSON back to dictionary
parsed_data = json.loads(json_data)
print(f"Parsed data: {parsed_data}")

# Writing JSON data to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # indent for better readability

print("JSON data has been written to data.json")

# Reading JSON data from the file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(f"Loaded data from file: {loaded_data}")
