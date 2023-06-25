import json

# Read JSON data from file
with open('tableDataasJson.json', 'r') as file:
    json_data = file.read()

# Parse JSON data
data = json.loads(json_data)

# Group the "Group in PP" values by "UserId" and count the items
grouped_data = {}
for item in data:
    user_id = item["UserId"]
    group = item["Group in PP"]
    if user_id in grouped_data:
        grouped_data[user_id]["Group in PP"].append(group)
        grouped_data[user_id]["Count"] += 1
    else:
        grouped_data[user_id] = {"Group in PP": [group], "Count": 1}

# Create final output JSON
output_data = []
for user_id, values in grouped_data.items():
    group_count = values["Count"]
    groups = values["Group in PP"]
    output_data.append({"UserId": user_id, "Group in PP": groups, "AccessGroupCount": group_count})

# Save final output as JSON file
output_file_path = 'output_2.json'  # Specify the output file path
with open(output_file_path, 'w') as output_file:
    json.dump(output_data, output_file, indent=4)

print("Output saved as:", output_file_path)