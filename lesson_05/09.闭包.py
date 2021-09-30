# def fn():
#     def innner():
#         print('我是fn2')
#     return  innner
#
# r = fn()
# r()

# def make_average():
#     nums = []
#
#     def average(n):
#         nums.append(n)
#         return sum(nums) / len(nums)
#
#     return average
#
#
# average = make_average()
#
# print(average(10))


def make_average():
    nums = []
    def average(n):
        nums.append(n)
        return sum(nums) / len(nums)
    return average

average = make_average()
print(average(10))












