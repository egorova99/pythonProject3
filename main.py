import os

base_path = os.getcwd()
file_name1 = '1'
file_name2 = '2'
file_name3 = 'Итог'
log_dir = 'files'
full_path = os.path.join(base_path, log_dir, file_name1)
full_path2 = os.path.join(base_path, log_dir, file_name2)
full_path3 = os.path.join(base_path, log_dir, file_name3)

class Files:
 def file_worker(encoding: str):
   file_name = full_path
   mode = 'r'
   with open(file_name, mode, encoding=encoding) as file:
     x = file.readlines()
     log_str = f'имя файла: {file_name1}.txt\nкол-во строк: 2\n{x[0]}{x[1]}'
     print(log_str)
   file_name = full_path2
   with open(file_name, mode, encoding=encoding) as file:
     y = file.readlines()
     log_str2 = f'имя файла: {file_name2}.txt\nкол-во строк: 1\n{y[0]}'
     print(log_str2)
   file_name = full_path3
   mode = 'w'
   with open(file_name, mode, encoding=encoding) as file:
     log_str3 = f'{log_str}\n{log_str2}'
     file.write(log_str3)
     file.close()


my_file = Files
my_file.file_worker('utf-8')

