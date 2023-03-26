from BTrees.OOBTree import OOBTree


class BTree_Class:

    bt = OOBTree()

    @staticmethod
    def add_Node(key, value):  # добавление пары ключ-значение
        BTree_Class.bt[key] = value


    @staticmethod
    def print_Tree():  # вывести всё дерево
        BTree_Class.check()
        for answer in BTree_Class.check():
            if answer == -1:
                print("Отказано")
            else:
                for pair in BTree_Class.bt.iteritems():
                    print(pair)

    @staticmethod
    def check():  # проверка на пустоту
        if len(BTree_Class.bt) == 0:
            answer = -1
            yield answer
        else:
            answer = 1
            yield answer

    @staticmethod
    def key_value(key):  # поиск по ключу
        BTree_Class.check()
        for answer in BTree_Class.check():
            if answer == -1:
                print("Отказано")
            else:
                if key in BTree_Class.bt:
                    print(BTree_Class.bt[key])
                else:
                    print("Такого ключа не существует")

    @staticmethod
    def remove_key(key):  # удаление по ключу
        BTree_Class.check()
        for answer in BTree_Class.check():
            if answer == -1:
                print("Отказано")
            else:
                del BTree_Class.bt[key]

    @staticmethod
    def remove_all():  # очистка древа
        BTree_Class.check()
        for answer in BTree_Class.check():
            if answer == -1:
                print("Дерева не существует")
            else:
                for i in list(BTree_Class.bt.keys()):
                    del BTree_Class.bt[i]
            print("Дерево удаленно")

