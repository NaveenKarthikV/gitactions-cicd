import os
import shutil

def compare_and_update(other_branch_folder, main_branch_folder):
    for root, _, files in os.walk(other_branch_folder):
        relative_path = os.path.relpath(root, other_branch_folder)
        main_folder = os.path.join(main_branch_folder, relative_path)
        
        for file in files:
            new_file_path = os.path.join(root, file)
            main_file_path = os.path.join(main_folder, file)
            
            if not os.path.exists(main_file_path) or not filecmp.cmp(new_file_path, main_file_path):
                shutil.copy(new_file_path, main_file_path)
                print(f"Updated {main_file_path}")
                
def main():
    new_branch_folder = "path/to/other-branch"
    main_branch_folder = "path/to/main-branch"
    
    compare_and_update(other_branch_folder, main_branch_folder)

if __name__ == "__main__":
    main()
