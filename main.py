import os


base_path = os.getcwd()
file_name1 = '1'
file_name2 = '2'
file_name3 = 'Итог'
log_dir = 'files'
full_path = os.path.join(base_path, log_dir, file_name1)
full_path2 = os.path.join(base_path, log_dir, file_name2)
full_path3 = os.path.join(base_path, log_dir, file_name3)

def file_worker(mode: str, encoding: str):
    log_text = ''
    file_name = full_path
    with open(file_name, mode, encoding=encoding) as file:
        x = file.readlines()
        log_str1 = f'имя файла: {file_name1}.txt\nкол-во строк: 2\n{x[0]}{x[1]}'
        print(log_str1)
    file_name = full_path2
    with open(file_name, mode, encoding=encoding) as file:
        y = file.readlines()
        log_str2 = f'имя файла: {file_name2}.txt\nкол-во строк: 1\n{y[0]}'
        print(log_str2)
    file_name = full_path3
    log_text = f'{log_str1}\n{log_str2}'
    return log_text

def file_write(mode: str, encoding: str):
    write_text = log_text
    file_name = full_path3
    with open(file_name, mode, encoding=encoding) as file:
        file.write(write_text)
        file.close()


log_text = file_worker('r', 'utf-8')
file_write('w', 'utf-8')

