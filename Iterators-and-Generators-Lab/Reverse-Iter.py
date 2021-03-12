class reverse_iter:
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)

    def __iter__(self):
        return self

    def __next__(self):
        self.length -= 1
        if self.length < 0:
            raise StopIteration
        return self.nums[self.length]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
