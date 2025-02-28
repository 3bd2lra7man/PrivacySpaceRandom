import os

def replace_string_in_file(file_path, target_string, replacement_string):
    try:
        if __file__ == file_path:
            return
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if target_string in content:
            content = content.replace(target_string, replacement_string)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Replaced in: {file_path}")
    except UnicodeDecodeError:
        None
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def walk_and_replace(directory, target_string, replacement_string, file_extensions=None):
    for root, _, files in os.walk(directory):
        for file in files:
            if file_extensions and not file.endswith(tuple(file_extensions)):
                continue  # Skip files that are not in the specified extensions
            file_path = os.path.join(root, file)
            replace_string_in_file(file_path, target_string, replacement_string)

if __name__ == "__main__":
    search_directory = "./"
    current_package = "cn.geektang.privacyspace"
    hidden_package = "com.privacyspace.hidden"

    walk_and_replace(search_directory, current_package, hidden_package)
