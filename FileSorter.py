import os

moduleTitle = "Computer Science"
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
fileDir = os.path.join(desktop, moduleTitle)


folders = {}
directories = []

def create_folders():
    if not (os.path.exists(fileDir)):
        os.makedirs(fileDir)

    if (os.path.isfile(fileDir + "\\filePrefixes.txt")):
        num_lines = sum(1 for line in (fileDir + "\\filePrefixes.txt"))
        if num_lines == 0:
            print("filePrefixes is empty, please enter prefixes before running sort")

        path = open(fileDir + "\\filePrefixes.txt", "r")
        for line in path:
            # get rid of trailing new line character
            line = line.replace('\n', '')

            # make the name of the folder a new path
            folders[os.path.join(fileDir, line)] = line

        for key in folders:
            if not os.path.exists(key):
                os.makedirs(key)
                print("Created Directory {}".format(key))
            else:
                print("\t{} already exists".format(key))
    else:
        path = open(fileDir + "\\filePrefixes.txt", "w+")
        print("filePrefixes.txt doesn't exist, creating, re-run script.")

def sort():
    for file in os.listdir(desktop):
        for key, values in folders.items():
            if file.startswith(values):
                newPath = key
                os.rename(desktop + "\\" + file, newPath + "\\" + file)
create_folders()
sort()