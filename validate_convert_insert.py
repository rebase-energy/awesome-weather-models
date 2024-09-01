import json

def check_fields(data, fields):
    print("Checking that all fields are present in data.")
    for i, d in enumerate(data): 
        for field in fields: 
            if field not in d.keys():
                print("Field {} not found in data[{}]".format(field, i))

def sort_alphabetically(data): 
    print("Sorting data by name alphabetically.")
    data.sort(key=lambda x: x["name"].lower())
    return data

def validate_table(data):
    fields = ["name", "description", "links"]

    check_fields(data, fields)
    data = sort_alphabetically(data)
    return data

# Function to convert JSON data to a Markdown table
def convert_table(json_data, mapping):
    # Extracting headers
    headers = ["name", "description", "code", "links"]
    alignments = {"name": ":---", "description": ":---", "code": ":---:", "problem_type": ":---:", "model_type": ":---:", "energy_assets": ":---:", "scale": ":---:", "links": ":---:"}

    include_headers = ["name", "description", "code", "links"]
    alignments = [alignments[header] for header in include_headers]

    display_headers = convert_string(include_headers)

    header_row = '| ' + ' | '.join(display_headers) + ' |'
    separator_row = '| ' + ' | '.join(alignments) + ' |'

    # Extracting rows
    rows = []
    for idx_entry, entry in enumerate(json_data):
        row = "|"
        missing_keys = [key for key in headers if key not in entry.keys()]
        if missing_keys:
            print(missing_keys)
            raise ValueError(f"Error in element at index {idx_entry}: Missing keys {missing_keys}")
        
        for header in include_headers:
            if header == "name":
                row = row + "`" + str(entry[header]) + "`"
            if header == "description":
                row = row + str(entry[header])
            if header == "code":
                if "code_license" in entry[header].keys():
                    row = row + str(entry[header]["code_license"])
            if header in mapping:
                for idx_key, key in enumerate(entry[header]):
                    row = row + mapping[header][key]
                    if idx_key < len(entry[header])-1: row = row + " "
            if header in ["links"]:
                for idx_key, key in enumerate(entry[header]):
                    row = row + "[[" + key + "]]" + "(" + entry[header][key] + ")" 
                    if idx_key < len(entry[header])-1: row = row + ", "
            row = row + "|"

        rows.append(row)

    # Combining all parts into the final table
    markdown_table = '\n'.join([header_row, separator_row] + rows)

    # Save the Markdown table to a file
    with open("model_table.md", 'w') as file:
        file.write(markdown_table)


def insert_table(source_file="model_table.md", read_file="README_no_table.md", target_file="README.md", placeholder="<!-- table_placeholder -->"):
    with open(source_file, 'r') as f:
        table_content = f.read()

    with open(read_file, 'r') as f:
        target_content = f.read()

    new_content = target_content.replace(placeholder, table_content)

    with open(target_file, 'w') as file: 
        file.write(new_content)

def convert_string(old_list): 
    new_list = []
    for old_string in old_list:
        words = old_string.split('_')
        new_string = ' '.join(word.capitalize() for word in words)
        new_list.append(new_string)

    return new_list

def custom_json_dump(data, indent=2):
    def format_dict(d, level=1):
        indent_space = ' ' * (level * indent)
        items = []
        for key, value in d.items():
            if isinstance(value, dict):
                formatted_value = format_dict(value, level + 1)
                items.append(f'{indent_space}"{key}": {formatted_value}')
            elif isinstance(value, list):
                # Keep lists on the same line
                list_items = ', '.join(json.dumps(item) for item in value)
                items.append(f'{indent_space}"{key}": [{list_items}]')
            else:
                # Other types use the default json encoding
                items.append(f'{indent_space}"{key}": {json.dumps(value)}')
        return '{\n' + ',\n'.join(items) + f'\n{" " * ((level - 1) * indent)}}}'
    
    formatted_list = []
    for item in data:
        formatted_list.append(format_dict(item))
    
    # Combine formatted dictionaries into a single line for the top-level list
    return '[\n  ' + ',\n  '.join(formatted_list) + '\n]'


if __name__ == "__main__":
    # Read JSON data from a file
    with open('data.json', 'r') as f:
        data = json.load(f)

    with open('mapping.json', 'r') as f:
        mapping = json.load(f)

    # Validate and clean JSON data
    data = validate_table(data)

    # Write custom JSON file
    custom_json_string = custom_json_dump(data, indent=2)
    with open('data.json', 'w') as f:
        f.write(custom_json_string)

    # Convert JSON to Markdown table
    convert_table(data, mapping)

    # Insert the Markdown table into a README file
    insert_table()

    # Print success message
    print("Markdown table inserted into the README.")