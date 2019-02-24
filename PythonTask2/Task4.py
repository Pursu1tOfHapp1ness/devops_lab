if __name__ == "__main__":
    N, M = map(int, input().split(' '))
    while M < (3*N):
        print("M must be 3 times N!! Try again:")
        N, M = map(int, input().split(' '))
        continue
    String = [((2*i+1)*'.|.').center(M, '-') for i in range(N//2)]
    CenterString = ['WELCOME'.center(M, '-')]
    print('\n'.join(String + CenterString + String[::-1]))
