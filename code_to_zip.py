import os
import zipfile

# Path to the folders containing the photos
folder_paths = ['bottom_left', 'bottom_right', 'bottom_middle', 'top_left', 'top_right', 'top_middle', 'left_middle', 'right_middle','middle']

# Iterate over the folders
for folder_path in folder_paths:
    # Name of the resulting zip file
    zip_file_name = f'{folder_path}.zip'

    # Create a zip file object in write mode
    zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

    # Iterate over the files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is an image (you can modify this condition to suit your specific needs)
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                file_path = os.path.join(root, file)
                # Add the file to the zip file
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))

    # Close the zip file
    zip_file.close()

    print(f'Successfully created {zip_file_name}')
