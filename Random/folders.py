import os
root_path = '/home/cwmdavies/PycharmProjects/Random/Folders'
text_file = open('fold_list.txt', 'r')
folders = text_file.readlines()
stripped_folders = list(map(str.strip, folders))
print(stripped_folders)
for folder in stripped_folders:
    os.mkdir(os.path.join(root_path,folder))