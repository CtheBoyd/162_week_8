def count_seq():
    number = '2'
    while True:
        yield str(number)
        next_value = ''
        while len(number) > 0:
            first = number[0]
            count = 0
            while len(number) > 0 and number[0] == first:
                count += 1
                number = number[1:]
            next_value += '{}{}'.format(count, first)
        number = next_value

if __name__ =="__main__":
    gen = count_seq()
    for i in range(8):
        print(next(gen))