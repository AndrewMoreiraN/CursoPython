import os
import shutil


class ListOfFiles:
    def get_list_of_files(self, dir_name):
        try:
            list_of_file = os.listdir(dir_name)
            all_files = list()
            for entry in list_of_file:
                full_path = os.path.join(dir_name, entry)
                if os.path.isdir(full_path):
                    all_files = all_files + self.get_list_of_files(full_path)
                else:
                    all_files.append(full_path)
            return all_files
        except Exception as e:
            print(f'Error: {e}, get_list_of_files LIST_OF_FILES')

    @staticmethod
    def get_files_only(dir_name):
        try:
            list_of_file = os.listdir(dir_name)
            all_files = list()
            for entry in list_of_file:
                full_path = os.path.join(dir_name, entry)
                if os.path.isdir(full_path):
                    continue
                else:
                    all_files.append(full_path)
            return all_files
        except Exception as e:
            print(f'Error: {e}, get_files_only LIST_OF_FILES')

    @staticmethod
    def verify_if_file_exists(file, old_directory, new_directory):
        try:
            base = file.replace(f'{old_directory}\\', '')
            base, ext = os.path.splitext(base)
            dup = 0
            while True:
                if os.path.exists(os.path.join(new_directory, f'{base}{ext}')):
                    dst_path = os.path.join(new_directory, f'{base}{dup}{ext}')
                else:
                    dst_path = os.path.join(new_directory, f'{base}{ext}')
                if os.path.exists(dst_path):
                    dup += 1
                    continue
                shutil.move(file, dst_path)
                break
            return
        except Exception as e:
            print(f'Error: {e}, verify_if_files_exists LIST_OF_FILES')
