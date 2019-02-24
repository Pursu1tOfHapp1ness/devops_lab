if __name__ == '__main__':
    Answer = dict()
    list4values = list(input("Enter values of list: ").split(' '))
    list_for_keys = list(input("Enter keys of list: ").split(' '))
    if len(list4values) < len(list_for_keys):
        #  Insert None, if list doesn't have values for such keys count
        list4values.extend([None] * (len(list_for_keys)-len(list4values)))
    for i in range(len(list_for_keys)):
        keys, values = list_for_keys[i], list4values[i]
        Answer[keys] = values
    print("Your constructed library: ")
    print(Answer)
