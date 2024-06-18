
def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def remove_newlines(data):
    data_cleaned = []
    for line in data:
        data_cleaned.append(line.strip())
    return data_cleaned

if __name__ == "main":
    print('running main')