import os

os.chdir('/Users/joowo/Desktop/System Analysis and Design I')
# change directory to whichever folder the ppt is saved

# print(os.getcwd())
# checks current working directory


for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    file_name = file_name.split('_')
    course_name = file_name[0]
    session_no = file_name[1]
    session_title = ' '.join(file_name[2:])
    new_name = '{}-{}) {}{}'.format(course_name, session_no, session_title, file_ext)
    os.rename(file, new_name)

# Note that this will need to be edited for list indexes and formats...
# As after using it once, it is not immediately reusable as it raises an index error;
# The code will need to be re-written every time I need to use it for a new project, but there can be a good baseline
# For the vanilla codebase which I can tweak and use for each use case.
# Either way it was a good practice implementing this to organize the SAD I module.

