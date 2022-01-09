print("Audio file converter")
print("====================\n")

print("Importing required packages..")
from os import path, walk, sep, mkdir
import subprocess, sys

if len(sys.argv) != 4:
    raise "Missing arguments. Input directory, input type, and output type all required."

input_dir = sys.argv[1]
type_from = sys.argv[2]
type_to = sys.argv[3]

output_dir = "converted_audio_files"
if not path.isdir(output_dir):
    mkdir(output_dir)

print("Converting files..")
for subdir, dirs, files in walk("."):
    for filename in files:
        name_and_ext = filename.split('.')
        name = name_and_ext[0]

        if filename.endswith(type_from):
            fromfilepath = input_dir + '\\' + name + '.' + type_from
            tofilepath = output_dir + '\\' + name + '.' + type_to

            print(fromfilepath, '->', tofilepath)

            subprocess.call(['ffmpeg', '-i', fromfilepath, tofilepath])
