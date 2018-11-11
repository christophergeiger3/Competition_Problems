# Memoization/Caching Method

# This solution makes use of a phenomenon known as the Polynomial numbers,
# which I discovered can be used as a graphical description of this problem.

class PolynomialNum:

    def __init__(self, s):
        self.s = s  # s = sides_of_shape
        self.index = 1
        self.cache = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.cache) >= self.index:
            ret = self.cache[self.index-1]
            self.index += 1
            return ret
        else:
            n = self.index
            ret = n**2 * (self.s - 2) - (n*(self.s - 4))

            ret = (self.index, int(ret/2))
            self.cache.append(ret)
            self.index += 1

            return ret

    def __repr__(self):
        return "PolynomialNum(" + str(self.s) + ")"

    def clear(self):
        self.index = 1


accuracy = 5  # Num of polynomial iterators to generate, starting from s=3 (triangular numbers)
poly_list = [PolynomialNum(s) for s in range(3, accuracy+3)]

for T in range(int(input())):
    default_str = "CAT"
    n = int(input())
    # List of starting string lists  (since string mutation isn't a thing)
    starting_strs = [list(default_str + "GC"*i) for i in range(accuracy)]
    # starting_str[0] = CAT, [1] = CATGC, [2] = CATGCGC, ...

    significant_values = []  # To be filled with the greatest (index, value) pairs that have values leq to n
    for gen in poly_list:
        to_add = (1, 1)
        for index, value in gen:
            if value <= n:
                to_add = index, value
            else:
                break
        significant_values.append(to_add)

    leftover_list = [n - i[1] for i in significant_values]
    # Leftovers are the amount of times to increment the amount of CAT Degrees by one.
    # In other words, they're the amount of 'GT' to append to the default_str
    # e.g. a CAT string with 3 leftovers would be CATGTGTGT

    minimum_leftover_index = 0
    for index, leftover in enumerate(leftover_list):
        if leftover < 0:
            continue  # Case where the significant value is greater than n
        else:
            if leftover < leftover_list[minimum_leftover_index]:
                minimum_leftover_index = index

    # So now we should know the location of the proper starting string (the same as the minimum_leftover_index)
    # and how many 'GT's to append to it (the minimum leftover value). After that we just append the proper amount of
    # 'AT's, and that should give us the answer...

    ret = starting_strs[minimum_leftover_index]  # To be filled with the value to be returned (printed)
    for GT in range(leftover_list[minimum_leftover_index]):
        ret.append("GT")

    for AT in range(significant_values[minimum_leftover_index][0]-1):  # ToDo: remove -1?
        # Add an amount of 'AT's equivalent to the index produced
        ret.append("AT")

    ret = ''.join(ret)
    [i.clear() for i in poly_list]
    print(ret)

