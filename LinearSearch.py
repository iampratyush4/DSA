def linear_search(numlist,find):
    for index,element in enumerate(numlist):
        if element == find:
            return index
    return 

if __name__ == "__main__":
    numlist=[12,4345,546,654,643,643,3,5,75]
    find=5
    indexlinear =linear_search(numlist,find)
    print(f"Number found at index {indexlinear} using linear search")

# linear_search
   
