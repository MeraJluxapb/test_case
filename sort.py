# функция слияния массивов по неубыванию
def merge(a, b):
    res = []
    len_a = len(a)
    len_b = len(b)

    i = 0
    j = 0
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    # если один из массивов больше другого, то прибавляем к результату оставшиеся числа,
    # т.к. они всегда больше последнего добавленного числа
    res += a[i:] + b[j:]
    return res


# рекурсивная фукнция разделения массива на 2 половины - выполняется до тех пор, пока не останется по 1 числу,
# которые "слепляются" по неубыванию с помощью функции merge
def merge_sort(array):
    pivot = len(array) // 2
    left = array[:pivot]
    right = array[pivot:]

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    return merge(left, right)
