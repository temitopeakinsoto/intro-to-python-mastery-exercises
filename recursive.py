def recursive_search(myList, number):
    #base case
    for i in range(0, len(myList)):
     if myList[i] == number:
        return "found"
     else:         
        return recursive_search(myList[1:], number)
 
num_list = [1,2,3,4,5]
print(recursive_search(num_list,9))