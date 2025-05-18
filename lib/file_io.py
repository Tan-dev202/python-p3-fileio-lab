def write_file(file_name='fruit_basket', file_content='Log 1: 6 apples added'):
    with open(f'{file_name}.txt',  mode='w', encoding='utf-8') as file_name:
        file_name.write(file_content)
    

def append_file(file_name='fruit_basket', append_content='Log 2: 3 pears removed'):
    with open(f'{file_name}.txt',  mode='a', encoding='utf-8') as file_name:
        file_name.write(append_content)
    

def read_file(file_name='fruit_basket'):
    with open(f'{file_name}.txt',  mode='r', encoding='utf-8') as file_name:
        return file_name.read()
    