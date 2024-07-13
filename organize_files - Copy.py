import os
import shutil

def organize_files(directory):
    # Iterate over all folders in the given directory
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        
        # Check if the item in the directory is a directory and not a file
        if os.path.isdir(folder_path):
            # Check if the folder contains a PNG file
            png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
            if png_files:
                # Assume there's only one PNG file per folder for simplicity
                filename = png_files[0]
                
                # Create folder A inside the existing folder
                folder_a_path = os.path.join(folder_path, 'B')
                os.makedirs(folder_a_path, exist_ok=True)
                
                # Move the PNG file into folder A
                src_file = os.path.join(folder_path, filename)
                dst_file = os.path.join(folder_a_path, filename)
                shutil.move(src_file, dst_file)
                print(f'Moved {filename} to {folder_a_path}')

if __name__ == '__main__':
    # Get the current directory where this script is located
    current_directory = os.getcwd()
    organize_files(current_directory)
