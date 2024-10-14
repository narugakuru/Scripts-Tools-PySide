# 批量复制文件列表，包括文件夹结构
import os
import shutil

origin_path = r"Z:\ssl-htdocs"
copy_path = r"E:\WorkSpace\WebKaisyu\html_1014"

# String of file paths (could be from a file or input)
raw_file_paths = """
/info/public/demand.html
/info/personal/index.html
/info/personal/stop1.html
/info/personal/demand.html
/info/personal/note1.html
/info/personal/stop2.html
/info/personal/note3.html
/pr/newPublic.html
/pr/study/index.html
/effort/standard.html
/form/opinion/index.html
/general/accessibility_result.html
/report/new/index.html
/pr/kensa/result/5.html
/report/zuiji/24.html
/report/zuiji/23.html
/report/zuiji/22.html
/report/demand/index.html
/proc/info/consult/order/06.html
/proc/info/consult/order/05.html
/proc/info/consult/sikaku/r05_06.html
/proc/info/item/index.html
/proc/info/item/order/06.html
/proc/result/consult/index.html
/proc/result/consult/public/06.html
/proc/result/item/index.html
/info/public/index.html
"""

# Function to normalize paths
def normalize_paths(raw_paths):
    normalized_paths = []
    
    # Split the raw string by lines and process each line
    for path in raw_paths.strip().splitlines():
        # Strip whitespace, replace backslashes with forward slashes, and ensure it starts with a forward slash
        path = path.strip().replace("\\", "/")
        if not path.startswith("/"):
            path = "/" + path
        normalized_paths.append(path)
    
    return normalized_paths

# Function to copy files and recreate folder structure
def copy_files_with_structure(origin_path, copy_path, file_paths):
    
    os.makedirs(os.path.dirname(copy_path), exist_ok=True)
    
    for file in file_paths:
        # Remove leading '/' to avoid issues with os.path.join
        file = file.lstrip('/')
        
        # Get full path of the source file
        source = os.path.join(origin_path, file)
        
        # Check if the source is a file and exists
        if os.path.isfile(source):
            # Create the target file path
            target = os.path.join(copy_path, file)
            
            # Create directories in the target path if they don't exist
            os.makedirs(os.path.dirname(target), exist_ok=True)
            
            # Copy the file to the target location
            shutil.copy2(source, target)
            print(f"Copied: {source} -> {target}")
        else:
            print(f"Skipped: {source} (Not a file)")


# Normalize the file paths
file_paths = normalize_paths(raw_file_paths)

# Run the function to copy files
copy_files_with_structure(origin_path, copy_path, file_paths)
