import os
dir_path = r'D:\python\VaraPython\PyCharm Community Edition 2022.1.2\EmailBot\Music'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

