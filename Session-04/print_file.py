from pathlib import Path
FILENAME = "RNU6_269P.txt" #we write the filename in capital letters to form a constant
#open and read the file
file_contents = Path(FILENAME).read_text()
print(file_contents)
