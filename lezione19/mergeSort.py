def mergeSort(input_list):

    if len(input_list) == 1:
        return input_list
    mid = len(input_list) // 2
    list_1 = mergeSort(input_list = input_list[:mid])
    list_2 = mergeSort(input_list = input_list[mid:])
    return merge(list_1,list_2)

def merge(list_1,list_2):
    i,j = 0 , 0 
    result = [None for _ in range(len(list_1 + list_2))]
    for k in range(len(result)):
        if list_1[i] > list_2[j]:
            result[k] = list_2[j]
            j += 1
        else:
            result[k] = list_1[i]
            i += 1

if __name__ == "__main__":
    input_list: list[int] = [0,1,2,3,4,5,6,7]
    mergeSort(input_list =  input_list)


