from os import walk, path, rename, makedirs
from shutil import rmtree
from string import ascii_lowercase
from random import choice

def random_string(length = 4):
    return ''.join(choice(ascii_lowercase) for _ in range(length))

def random_package_name():
    package_parts = [random_string() for _ in range(3)]
    return '.'.join(package_parts)

def replace_string_in_file(file_path, target_string, replacement_string):
    try:
        this = path.abspath(__file__)
        rfile_path = path.abspath(file_path)
        
        if this == rfile_path:
            print("Skipping self")
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
    for root, _, files in walk(directory):
        for file in files:
            if file_extensions and not file.endswith(tuple(file_extensions)):
                continue  # Skip files that are not in the specified extensions
            file_path = path.join(root, file)
            replace_string_in_file(file_path, target_string, replacement_string)

def rename_package_dir(random_package: str):
    # Define the old and new paths for main and test directories
    package_path1 = "./app/src/main/java/cn/geektang/privacyspace"
    package_path2 = "./app/src/test/java/cn/geektang/privacyspace"
    new_package_path1 = path.join("./app/src/main/java", random_package.replace(".", "/"))
    new_package_path2 = path.join("./app/src/test/java", random_package.replace(".", "/"))

    try:
        # Create parent directories for the new paths if they don't exist
        makedirs(path.dirname(new_package_path1), exist_ok=True)
        makedirs(path.dirname(new_package_path2), exist_ok=True)

        # Rename the directories
        rename(package_path1, new_package_path1)
        print(f"Renamed: {package_path1} -> {new_package_path1}")
        rename(package_path2, new_package_path2)
        print(f"Renamed: {package_path2} -> {new_package_path2}")
        rmtree("/app/src/main/java/cn/")
        rmtree("/app/src/test/java/cn/")
    except FileNotFoundError:
        print(f"Directory not found: {package_path1}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_directory = "./"
    current_package = "cn.geektang.privacyspace"
    random_package = random_package_name()
    print(f"Current package: {current_package}")
    print(f"Random package: {random_package}")
    walk_and_replace(search_directory, current_package, random_package)
    rename_package_dir(random_package)
