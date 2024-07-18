# Реализуем построчный процесс чтения
def process_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Обработка строки
            process_line(line)

def process_line(line):
    # В данной функции реализуем логику обработки строки
    print('Логика обработки строки')