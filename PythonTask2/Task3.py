def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    Input = open(r'C:\\Users\\unles\\Desktop\\INPUT.txt')
    num = int(Input.read())
    Output = open(r'C:\\Users\\unles\\Desktop\\OUTPUT.txt', "w")
    Output.write(str(factorial(num)))
    Input.close()
    Output.close()
