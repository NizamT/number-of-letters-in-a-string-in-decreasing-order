def most_frequent(name):
    unsorted_dic = {}
    most_frequent_dic = {}
    for intex in range(len(name)):
        if name[intex] not in unsorted_dic.keys():
            unsorted_dic[name[intex]] = name.count(name[intex])
    sorted_values = reversed(sorted(unsorted_dic.values()))

    for values in sorted_values:
        for keys in unsorted_dic.keys():
            if unsorted_dic[keys] == values:
                most_frequent_dic[keys] = values
    print("Output :", end=" ")
    for key, value in most_frequent_dic.items():
        print(f'{key}={value}', end=" ")


name = input("input : ")
most_frequent(name)
