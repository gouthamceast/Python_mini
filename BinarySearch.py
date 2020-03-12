lst = [x for x in map(int,(input()).split(' '))]

arr = sorted(lst)

print('sorted array ', arr)
count = len(arr)

print('count ',count)

user_input = int(input("Enter the number you want to find"))

def bin_search(sorted_list,length,user_input):
    start = 0
    end = length-1
    while start<end:
        mid = (start+end)//2
        if user_input == sorted_list[mid]:
            print('\n Entered number is found at position {}'.format(mid))
            return -1
        elif user_input <= sorted_list[mid]:
            end = mid-1
        elif user_input >= sorted_list[mid]:
            start = mid+1
    print('\n Element not found')
    return -1

bin_search(arr,len(arr),user_input)

