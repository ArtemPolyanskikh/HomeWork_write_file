with open('text1.txt', 'r', encoding='utf-8') as t1, open('text2.txt', 'r', encoding='utf-8') as t2, open('text3.txt', 'r', encoding='utf-8') as t3, open('text4.txt', 'a', encoding='utf-8') as t4 :

    f_list = {t1: 'text1.txt', t2: 'text2.txt', t3: 'text3.txt'}
    res = sorted(f_list, key=lambda x: len(x.readlines()))
    t1.seek(0)
    t2.seek(0)
    t3.seek(0)

    for file in res:
        t4.write(f'{f_list[file]}\n')
        t4.write(f'{len(file.readlines())}\n')
        file.seek(0)
        t4.writelines(file.readlines())
        t4.write('\n')

    print(res)



    