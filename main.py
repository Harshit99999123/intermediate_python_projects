import os
import shutil


# TAKE INPUT PATH FROM THE USER
# VALIDATE THE PATH
# GO THROUGH FILES IN THE FOLDER AND SEGREGATE THEM BY MOVING THEM INTO DIFFERENT FOLDERS BASED ON THEIR EXTENSIONS
# DELETE THE EMPTY FOLDERS THAT REMAINED


def is_directory_empty(directory_path: str) -> bool:
    return len(os.listdir(directory_path)) == 0


def delete_empty_folders(source_path: str):
    for curr_dir, list_of_subdirs, list_of_filenames in os.walk(source_path, topdown=False):
        for present_dir in list_of_subdirs:
            present_dir_path: str = os.path.join(curr_dir, present_dir)
            if is_directory_empty(present_dir_path):
                os.rmdir(present_dir_path)


def sort_files(source_path: str):
    for curr_dir, list_of_subdir, list_of_files in os.walk(source_path):

        for file_name in list_of_files:
            name, extension = os.path.splitext(file_name)
            target_folder_name: str = extension[1:]
            target_folder_path: str = os.path.join(source_path, target_folder_name)
            #check if folder exists
            if not os.path.exists(target_folder_path):
                #create new folder
                os.makedirs(target_folder_path)
            file_path: str = os.path.join(curr_dir, file_name)
            target_file_path: str = os.path.join(target_folder_path, file_name)
            # check if target file path is already there
            if not os.path.exists(target_file_path):
                # move files in the folder
                shutil.move(file_path, target_folder_path)
            else:
                print(f"{target_file_path} already exists.")


# MAIN METHOD TO DRIVE THE CODE
def main():
    user_input = input("Please provide the absolute file path to sort: ")

    if os.path.exists(user_input):
        sort_files(user_input)
        delete_empty_folders(source_path=user_input)
    else:
        raise Exception("Invalid file path entered.")


if __name__ == '__main__':
    main()
