import os
import shutil

def organize_files(directory):
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file is a PNG
        if filename.endswith('.png'):
            # Create a folder name based on the file name (without the .png extension)
            folder_name = os.path.splitext(filename)[0]
            folder_path = os.path.join(directory, folder_name)
            
            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
            
            # Move the file into the new folder
            src_file = os.path.join(directory, filename)
            dst_file = os.path.join(folder_path, filename)
            shutil.move(src_file, dst_file)
            print(f'Moved {filename} to {folder_path}')

if __name__ == '__main__':
    # Specify the directory containing the PNG files
    directory = os.getcwd()
    organize_files(directory)
