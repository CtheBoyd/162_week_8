# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date:7/28/2022
# Description: Generator function. that doesn't require any arguments and generates a sequence
# that starts like this: 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112, ...
#


def count_seq():
    yield "2"
    yield "12"
    value = 3
    while True:
        nums = "12"
        for i in range(3, value+1):
            nums += "$"
            length = len(nums)
            count = 1
            temp = ""
            for y in range(1, length):
                if nums[y] != nums[y-1]:
                    temp += str(count)
                    temp += nums[y-1]
                    count = 1
                else:
                    count += 1
            nums = temp
        yield nums
        value += 1



if __name__ =="__main__":
    gen = count_seq()
    for i in range(8):
        print(next(gen))