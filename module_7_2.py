
def custom_write(file_name, strings):
    strings_positions = {}
    file_name = 'test.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            position = file.tell()
            file.write(string + '\n')
            key_ = (len(strings_positions) + 1, position)
            strings_positions[key_] = string
    return strings_positions


info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

