import os
import shutil

def organize_files(directory):
    # Define the mapping of file types to directories
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Music': ['.mp3', '.wav', '.flac', '.aac'],
        'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
        'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
        'Scripts': ['.py', '.js', '.sh', '.bat']
    }

    # Create subdirectories if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file type and move to the corresponding directory
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                moved = True
                break

        # If the file type is not recognized, move it to an 'Others' folder
        if not moved:
            other_folder = os.path.join(directory, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))

    print("Files organized successfully.")

# Main function to run the script
if _name_ == "_main_":
    directory = input("Enter the directory path to organize: ")
    if os.path.exists(directory):
        organize_files(directory)
    else:
        print("The specified directory does not exist.")