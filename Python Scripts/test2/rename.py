import os

os.chdir('/Users/joowo/desktop/Python Scripts/test2')
# changes directory to the wd.

imgs = [".jpg", ".png", ".jfif", ".jpeg"]
documents = [".pdf", ".docx", ".doc", ".txt", ".md", ".ppt"]
executable = [".exe"]

for file in os.listdir():
    # print(f) # iterates through all the file_name in the working directory and prints f.
    # print(os.path.splitext(f))  # splits filename into a tuple.
    file_name, file_ext = os.path.splitext(file)
    # assigns each part of the tuple for each filename and extension into
    # different variables, so that now we can get file_name separately
    print(file_ext)



# print(os.getcwd())
# checks current working directory
