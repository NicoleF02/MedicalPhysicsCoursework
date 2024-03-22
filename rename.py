import os

def rename_file_to_last_two_parts(file_path):
    parts = file_path.split('/')
    
    new_file_name = parts[-2] + parts[-1].replace('EdMedPhysics.root', '.root')
    
    new_file_path = os.path.join(*parts[:-1], new_file_name)
    
    os.rename(file_path, new_file_path)
    
    print(f"File renamed to: {new_file_path}")

def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.root'):
                file_path = os.path.join(root, file)
                rename_file_to_last_two_parts(file_path)

# Renames all the edmedphys.root things to like bone.root etc...
directory_path = "."
rename_files_in_directory(directory_path)

