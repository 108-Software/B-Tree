import BTree


def main():
    print("Это программа для работы с ассоциативным бинарным В-древом")
    print("----------------------------------------------------------")
    print(" 0. Выход \n 1. Добавление элемента по ключу \n 2. Поиск по ключу \n "
              "3. Удаление по ключу \n 4. Очистить всё дерево \n 5. Вывести всё дерево")

    while True:

        answer = input()

        if answer == "0":
            break

        if answer == "1":
            print(" Введите ключ: ")
            key = input()
            print(" Введите значение ключа: ")
            value = input()
            BTree.BTree_Class.add_Node(int(key), int(value))



        if answer == "2":
            print(" Введите ключ: ")
            key = input()
            BTree.BTree_Class.key_value(int(key))


        if answer == "3":
            print(" Введите ключ: ")
            key = input()
            BTree.BTree_Class.remove_key(int(key))


        if answer == "4":
            BTree.BTree_Class.remove_all()


        if answer == "5":
            BTree.BTree_Class.print_Tree()



if __name__ == '__main__':
    main()