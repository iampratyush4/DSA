"""
Binary search follows the divide and conquer approach in which the list is divided into two halves, 
and the item is compared with the middle element of the list.
 If the match is found then, the location of the middle element is returned. 
Otherwise, we search into either of the halves depending upon the result produced through the match.
IT IS GENRALLY USED TO SEARCH IN A SORTED LIST.
"""

def binary_searchUsingloop(numlist,find):

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

def binary_searchRecursion(numlist,find,leftIndex,rightIndex):
    if rightIndex<leftIndex:
        return -1
     
    midIndex=(leftIndex+rightIndex)//2
    if midIndex>=len(numlist) or midIndex<=0:
        return -1

   
   
    midNum= numlist[midIndex]
    if midNum== find:
        return midIndex
    
    if midNum<find:
        leftIndex=midIndex+1
    else:
        rightIndex=midIndex-1
    
    return binary_searchRecursion(numlist,find,leftIndex,rightIndex)

    return

if __name__ == "__main__":
    numlist= [12,4345,546,654,643,643,3,5,75]
    sortedlist=sorted(numlist)
    print(numlist)
    print(sortedlist)
    find=5
    indexbinary1 =binary_searchUsingloop(sortedlist,find)
    print(f"Number found at index {indexbinary1} using binary search while loop")
    indexbinary2 =binary_searchRecursion(sortedlist,find,0,len(sortedlist))
    print(f"Number found at index {indexbinary2} using binary search recursion")
