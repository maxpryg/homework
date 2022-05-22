import os


def string_numerator():
    """Считывает содержимое файла, добавляет к считанным строкам порядковый
    номер и сохранять их в таком виде в новом файле. Имя исходного и целевого
    файла запрашивается у пользователя."""
    # цикл для запроса исходного файла
    while True:
        input_file_name = input("Введи имя исходного файла: ")
        if os.path.isfile(input_file_name):
            break
        else:
            print("Такого файла не существует\n")

    # цикл для запроса целевого файла
    while True:
        output_file_name = input("Введи имя целевого файла: ")
        if os.path.isfile(output_file_name):
            print("Файл с таким именем существует.")
            ans = input("Перезаписать его? y/n: \n")
            if ans in "Yy":
                break
        else:
            break

    counter = 1
    with open(input_file_name, 'r') as input_file,\
            open(output_file_name, 'w') as output_file:
        for line in input_file:
            output_file.write(str(counter) + ': ' + line)
            counter += 1


if __name__ == "__main__":
    string_numerator()
