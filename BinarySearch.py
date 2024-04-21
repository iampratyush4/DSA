"""
Binary search follows the divide and conquer approach in which the list is divided into two halves, 
and the item is compared with the middle element of the list.
 If the match is found then, the location of the middle element is returned. 
Otherwise, we search into either of the halves depending upon the result produced through the match.
"""

def binary_search(numlist,find):

    leftIndex=0
    rightIndex= len(numlist)-1
    midIndex=0
     
    while leftIndex <= rightIndex:
        midIndex= (leftIndex+rightIndex) // 2
        midNum=numlist[midIndex]

        if midNum==find:
            return midIndex
        
        if midNum< find:
            leftIndex=midIndex+1

        else:
            rightIndex=midIndex-1

    return -1

if __name__ == "__main__":
    numlist= [12,4345,546,654,643,643,3,5,75]
    sortedlist=sorted(numlist)
    print(numlist)
    print(sortedlist)
    find=5
    indexbinary =binary_search(sortedlist,find)
    print(f"Number found at index {indexbinary} using binary search")
