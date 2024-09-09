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
def convert_table(json_data, mapping, table_name):
    # Extracting headers
    headers = ["name", "description", "open_source", "links"]
    alignments = {"name": ":---", "description": ":---", "open_source": ":---:", "links": ":---:"}

    include_headers = ["name", "description", "open_source", "links"]
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
                row = row + "`" + str(entry[header]) + "`"
            if header == "description":
                row = row + str(entry[header])
            if header in ["operational_data", "open_source", "open_weights"]:
                row = row + mapping[str(entry[header])]
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
    convert_table(data_ai_models, mapping, "ai_models.md")

    # Insert the Markdown table into a README file
    insert_table("ai_models.md")