"""
os is a built-in Python module that provides a way of using operating system-dependent functionality — like reading environment variables, working with the file system (paths, directories, files), and getting system info.
"""
import os
print(os.getcwd()) # Get the current working directory

"""
Reading files.
"""

print("Opening Files")
print("=============")

# Open takes a filename and a mode
openfile = open("2.Python_Data_Representations/Module_4/text_file.txt", "rt")

# Modes for reading:
#  r - read (default)
#  t - text (default)
#  b - binary

print(type(openfile))
print(openfile)

# Must close file after opening it
openfile.close()

print("")
print("Errors")
print("======")

# nofile = open("nosuchfile.txt")

print("")
print("Reading")
print("=======")

datafile = open("2.Python_Data_Representations/Module_4/text_file.txt", "rt")

data = datafile.read()

print("type:", type(data))
print("length:", len(data))
print("")
print(data)

datafile.close()