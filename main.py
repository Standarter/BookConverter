import os

size = 10 * 1024
files = os.listdir(os.getcwd())
iterations = 1

print(os.getcwd())

for file in files:
    file = file.split(".")
    if file[1] == 'pdf':
        print(str(iterations) + ") " + "Starting converting [" + file[0] + "] - " + str(int(os.stat(file[0] + "." + file[1]).st_size)/int(1032333)))
        os.system("konsole -e pdf2djvu " + os.getcwd() + "/" + file[0] + ".pdf" + " -o " + os.getcwd() + "/" + file[0] + ".djvu")
        os.remove(file[0] + ".pdf")
        print(str(iterations) + ") = COMPLETE")
        iterations += 1