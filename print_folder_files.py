import os 

# loop through the list of folders
# check if the folder exists
# if the folder does not exist, print an error message
def list_files_folder (folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "The Folder does not exist"
    except PermissionError:
        return None, "You do not have permission to access the folder" 
                                 
# ask the user to enter the folder names
# split the folder names into a list
def main():
    folders = input ("Please enter the folder names with space in between:").split()

    for folder in folders:
        files, error_message = list_files_folder(folder)
        if files:
            print (f"The files in {folder}:")
            for file in files:
                print (file)
        else:
            print (f"Error in {folder}: {error_message}")

if __name__== "__main__":
    main()


