def all_unique(array):
    return len(array) == len(set(array))

print(all_unique([1,2,3,4]))
print(all_unique([1,2,2,4]))
print(all_unique([]))