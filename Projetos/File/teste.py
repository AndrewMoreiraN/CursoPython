import concurrent.futures
import os
import re

from list_of_files import ListOfFiles

path = r'G:\musicas\com_mofo'
threads = 50
list_of_files = ListOfFiles()

list_files = list_of_files.get_files_only(path)


def rename(list_of_file):
    try:
        temp = list_of_file
        temp = temp.replace(f'{path}\\', '')
        temp = re.sub(r"^(.*-)", '', temp)
        base, ext = os.path.splitext(temp)
        dup = 0
        while True:
            dst_path = os.path.join(path, f'{base}{dup}{ext}')
            if os.path.exists(dst_path):
                dup += 1
                continue
            os.rename(list_of_file, dst_path)
            break
    except Exception as e:
        print(f'Error: {e} rename')


def renamer():
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            try:
                executor.map(rename, list_files)
            except Exception as e:
                print(f'Error: {e} renamer')
    except Exception as e:
        print(f'Error2: {e}')


renamer()
