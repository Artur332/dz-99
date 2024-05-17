def read_file(file_path):
    try:
        with open(file_path, 'f') as file:
            content = file.read()
            print('зміст файлу')
            print(content)
    except FileNotFoundError:
        print('файл не знайдено')


file_path = input("введіть шлях файлу")

read_file(file_path)