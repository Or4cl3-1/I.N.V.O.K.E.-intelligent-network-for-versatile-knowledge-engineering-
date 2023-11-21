import os
import re

def fix_indentation(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if re.match('^  ', lines[i]):
            lines[i] = lines[i].replace('  ', '    ', 1)

    with open(file_path, 'w') as file:
        file.writelines(lines)

fix_indentation('file2.py')
