def input_count():
    try:
        count = int(input("Enter length of set = "))
    except (ValueError, UnboundLocalError):
        print("Invalid literal for int()")
    return count


def create_set():
    try:
        set_example = set(map(int, input("Enter the values : ").split(' ')))
    except (ValueError, UnboundLocalError):
        print("Invalid literal for int()")
    return set_example


if __name__ == "__main__":
    count1 = input_count()
    set1 = create_set()
    count2 = input_count()
    set2 = create_set()
    set_final = set.symmetric_difference(set1, set2)
    for i in sorted(list(set_final)):
        print(i)
