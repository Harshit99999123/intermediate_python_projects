File Sorter Project

Overview

The File Sorter Project is a Python script that helps users organize their files by sorting them into different folders based on their extensions. It moves the files into respective directories, ensuring that the file names are preserved. Additionally, the script removes any empty directories that may remain after the sorting operation.

Features
	•	Sorts files in a given directory by file extension.
	•	Creates new folders based on file extensions (e.g., .txt, .pdf, .jpg).
	•	Moves the files into the corresponding folders.
	•	Deletes any empty directories left behind after sorting.
	•	Validates if the provided path exists before starting the operation.

Requirements
	•	Python 3.x
	•	os and shutil modules (part of the Python Standard Library)

 How It Works
	1.	Input Path: The script prompts you to enter an absolute path to a folder that contains the files you wish to sort.
	2.	File Sorting: The script categorizes files by their extensions and moves them into respective folders (e.g., .txt files will be moved to a txt folder).
	3.	Empty Folder Deletion: After the files are sorted, the script checks for and removes any empty directories that remain in the source folder.
	4.	Output: Files are moved and organized without modifying their names. Only the directory structure is changed.
