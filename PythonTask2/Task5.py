def moves(our_steps):
    x = 0
    y = 0
    for step in our_steps:
        if step == 'D':
            y -= 1
        elif step == 'U':
            y += 1
        elif step == 'L':
            x -= 1
        elif step == 'R':
            x += 1
    if x == 0 and y == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    steps = input("Enter robot's steps: ")
    print(moves(steps))
