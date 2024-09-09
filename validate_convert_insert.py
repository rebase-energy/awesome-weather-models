import json
from collections import OrderedDict
import jsonschema

def validate_table(data, schema):
    for entry in data:
        try:
            jsonschema.validate(instance=entry, schema=schema)
            print(f"JSON data is valid for model: {entry['name']}.")
        except jsonschema.exceptions.ValidationError as e:
            # Print the relevant information
            if 'name' in e.instance:
                print(f"JSON validation error in item with name: {e.instance['name']}")
            # Re-raise the exception to stop the execution
            raise e

def sort_items_alphabetically(data): 
    print("Sorting items by name alphabetically.")
    data.sort(key=lambda x: x["name"].lower())
    return data

def sort_keys(data, schema):
    print("Sorting keys by predefined order.")
    order = list(schema["properties"].keys())
    # Create a new dictionary with keys in the specified order
    sorted_data = []
    for entry in data:
        entry = {key: entry[key] for key in order if key in entry}
        sorted_data.append(entry)

    return sorted_data

def write_custom_json(data, name, indent=2):
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
        
        formatted_dict = '{\n' + ',\n'.join(items) + f'\n{" " * ((level - 1) * indent)}}}'
        return formatted_dict
    
    formatted_list = []
    for item in data:
        formatted_list.append(format_dict(item))
    
    output_json = '[\n  ' + ',\n  '.join(formatted_list) + '\n]'

    with open(name, 'w') as f:
        f.write(output_json)

# Function to convert JSON data to a Markdown table
def convert_table(json_data, mapping, line_info, table_name):
    # Extracting headers
    headers = ["name", "organization", "description", "open_source", "links"]
    alignments = {"name": ":---", "organization": ":---", "description": ":---", "operational_data": ":---:", "open_source": ":---:", "open_weights": ":---:", "links": ":---:"}

    include_headers = ["name", "organization", "operational_data", "open_source", "open_weights", "links"]
    #include_headers = ["name", "organization", "description", "operational_data", "open_source", "open_weights", "links"]
    
    permalink = "https://github.com/rebase-energy/awesome-weather-models/blob/a86f37f003e0e53a3035228e3eee0d7bbec8c26e/data_ai_models.json#"
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
            raise ValueError(f"Error in element at index {idx_entry}: Missing keys {missing_keys}")
        
        for header in include_headers:
            if header == "name":
                row = row + "[`" + str(entry[header]) + "`](" + permalink + f"L{line_info[entry[header]][0]}-L{line_info[entry[header]][1]})"
            if header in ["description", "organization"]:
                row = row + str(entry[header])
            if header in ["operational_data", "open_source", "open_weights"]:
                row = row + mapping[str(entry[header])] 
                if entry[header]:
                    row = row + " <br> " + str(entry[header.split("_")[1]+"_license"])
            if header in ["links"]:
                for idx_key, key in enumerate(entry[header]):
                    row = row + "[[" + key + "]]" + "(" + entry[header][key] + ")" 
                    if idx_key < len(entry[header])-1: row = row + ", "
            row = row + "|"

        rows.append(row)

    # Combining all parts into the final table
    markdown_table = '\n'.join([header_row, separator_row] + rows)

    # Save the Markdown table to a file
    with open(table_name, 'w') as file:
        file.write(markdown_table)

def extract_outermost_bracket_lines(json_file_path):
    with open(json_file_path, 'r') as f:
        lines = f.readlines()

    outer_object_start = None  # Stores the line number of the outermost opening bracket
    outer_object_end = None    # Stores the line number of the outermost closing bracket
    inside_outer_object = False  # Flag to indicate when we are inside the outer object

    line_numbers = {}  # Dictionary to hold {name: [opening_line, closing_line]}
    current_object_name = None

    # Loop through each line and check for outer brackets
    for line_num, line in enumerate(lines, start=1):
        stripped_line = line.strip()
        # Detect outermost opening bracket
        if "{" in stripped_line and not inside_outer_object:
            outer_object_start = line_num
            inside_outer_object = True
            continue

        # Look for the first key (object name) after the outermost opening bracket
        if inside_outer_object and "name" in stripped_line:
            key = stripped_line.split(":")[1].split('"')[1]

            # First key encountered after the opening bracket is the name
            if current_object_name is None:
                current_object_name = key

        # Detect the outermost closing bracket
        if "}" in stripped_line and inside_outer_object:
            outer_object_end = line_num
            inside_outer_object = False

            # Store the line numbers in the dictionary and reset
            if current_object_name:
                line_numbers[current_object_name] = [outer_object_start, outer_object_end]
                current_object_name = None
                outer_object_start = None
                outer_object_end = None

    return line_numbers

def convert_string(old_list): 
    new_list = []
    for old_string in old_list:
        words = old_string.split('_')
        new_string = ' '.join(word.capitalize() for word in words)
        new_list.append(new_string)

    return new_list

def insert_table(source_file, read_file="README_no_table.md", target_file="README.md", placeholder="<!-- table_placeholder -->"):
    with open(source_file, 'r') as f:
        table_content = f.read()

    with open(read_file, 'r') as f:
        target_content = f.read()

    new_content = target_content.replace(placeholder, table_content)

    with open(target_file, 'w') as file: 
        file.write(new_content)

    print("Markdown table inserted into the README.")

if __name__ == "__main__":
    # Read JSON data from a file
    with open('data_ai_models.json', 'r') as f:
        data_ai_models = json.load(f)

    with open('schema_ai_models.json', 'r') as f:
        schema_ai_models = json.load(f)

    with open('mapping.json', 'r') as f:
        mapping = json.load(f)

    # Validate and clean JSON data
    validate_table(data_ai_models, schema_ai_models)
    data_ai_models = sort_items_alphabetically(data_ai_models)
    data_ai_models = sort_keys(data_ai_models, schema_ai_models)

    # Write custom JSON file
    ai_models_json = write_custom_json(data_ai_models, "data_ai_models.json", indent=2)

    # Convert JSON to Markdown table
    line_info = extract_outermost_bracket_lines("data_ai_models.json")
    convert_table(data_ai_models, mapping, line_info, "ai_models.md")

    # Insert the Markdown table into a README file
    insert_table("ai_models.md")