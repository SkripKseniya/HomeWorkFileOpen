book =[]
with open('cookbook.txt', 'rt', encoding= 'utf8') as file:
    for name_dish in file:
        n_d = name_dish.strip()
        pice_list = []
        c_book = {n_d: pice_list}
        emploees_count = file.readline()
        for i in range(int(emploees_count)):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            pice_list.append({'ingredient_name': ingredient_name,
                              'quantity': quantity,
                              'measure': measure })
        blank_line = file.readline()
        book.append(c_book)

def get_shop_list_by_dishes(dishes, person_count):
    for x in book:
        for dish in dishes:
            if dish in x:
                for z in x.values():
                    for a in z:
                        # print(a)
                        ingredient_n = a['ingredient_name']
                        quantity_n = int(a['quantity'])*person_count
                        measure_n = a['measure']
                        # print(quantity_n, ingredient_n, measure_n)
                        list_shop = {ingredient_n: {
                              'quantity': quantity_n,
                              'measure': measure_n }}
                        print(list_shop)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

