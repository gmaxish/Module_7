"""
В файле nums.txt хранятся вещественные числа. Дописать в файл эти же числа, упорядочив их по возростанию.
"""

creat_file_name = "nums.txt"

n = [1.23, 4.51, 7.777, 2.1, 0.2, 9.76, 5.77, 12.4321]


def tostr(n):
    n = list(map(str, n))
    return " ".join(n)


with open(creat_file_name, "w") as f:
        f.write(tostr(n))

print("Done!")


read_file = "nums.txt"

with open(read_file, "r") as f:
    nums = f.read()
print(nums)

nums_list = sorted(list(map(float, nums.split())))
print(nums_list)


with open(read_file, "a") as f:
    f.write("\n")
    f.write(tostr(nums_list))
