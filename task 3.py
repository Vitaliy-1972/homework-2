def count_strings(files_list):
    dict_count_docs = {}
    for doc_txt in files_list:
        with open(doc_txt) as f:
            sum_string = len(f.readlines())
        dict_count_docs[doc_txt] = sum_string
    sorted_dict = dict(sorted(dict_count_docs.items(), key=lambda x: x[1]))
    return sorted_dict


def write_file():
    with open('sum.txt', 'a') as f:
        dict_files = count_strings(['1.txt', '2.txt', '3.txt'])
        for file, count in dict_files.items():
            f.write(f'\n{file}\n{count}\n')
            with open(file) as f1:
                a = f1.read()
            f.write(f'{a}')
    with open('sum.txt') as f:
        b = f.read()
    return b


print(write_file())
