# $python readfile.py filename
import fileinput

for f in fileinput.input():
    print(f)