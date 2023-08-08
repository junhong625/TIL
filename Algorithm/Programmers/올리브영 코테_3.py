# folders = [["food", "root"], ["meat", "food"], ["fruit", "food"], ["animal", "root"]]
# files = [["cat", "1B", "animal"], ["dog", "2B", "animal"], ["fork", "1KB", "meat"], ["beef", "8KB", "meat"], ["apple", "4B", "fruit"], ["fire", "83B", "root"]]
# selected = ["root", "meat"]
# excepted = ["fork", "apple"]
folders = [["animal", "root"], ["fruit", "root"]]
files = [["cat", "1B", "animal"], ["dog", "2B", "animal"], ["apple", "4B", "fruit"]]
selected = ["animal"]
excepted = ["apple"]

def sum_size(folder):
    if folder_structure[folder]["visited"]:
        return

    global total_size, total_cnt
    for file in folder_structure[folder]["files"]:
        if file in excepted:
            continue
        print(folder, file)
        total_size += file_info[file]
        total_cnt += 1

    folder_structure[folder]["visited"] = True

    if folder_structure[folder]["child"]:
        for f in folder_structure[folder]["child"]:
            sum_size(f)

from collections import defaultdict

answer = []

total_cnt = 0
total_size = 0

folder_structure = defaultdict(dict)
file_info = {}
for child, parent in folders:
    if parent not in folder_structure:
        folder_structure[parent] = {"child" : [], "files" : [], "visited" : False}
    if child not in folder_structure:
        folder_structure[child] = {"child" : [], "files" : [], "visited" : False}
    folder_structure[parent]["child"].append(child)

for name, size, folder in files:
    folder_structure[folder]["files"].append(name)
    file_info[name] = int(size[:-2]) * 1024 if "KB" in size else int(size[:-1])

for folder in selected:
    sum_size(folder)

print([total_size, total_cnt])