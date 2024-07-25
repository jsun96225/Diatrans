import os

def print_directory_structure(root_dir, indent="", file=None):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            file.write(f"{indent}{item}/\n")
            print_directory_structure(item_path, indent + "    ", file)
        else:
            file.write(f"{indent}{item}\n")

if __name__ == "__main__":
    root_directory = "."  # 当前目录
    with open("structure.txt", "w") as f:
        print_directory_structure(root_directory, file=f)
