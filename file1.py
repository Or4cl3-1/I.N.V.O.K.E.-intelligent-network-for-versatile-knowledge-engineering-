import os


def replace_tabs_with_spaces(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace('\t', '    ')
    with open(file_path, 'w') as file:
        file.write(content)

replace_tabs_with_spaces('file1.py')
