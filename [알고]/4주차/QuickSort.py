'''
QuickSort Algorithm

'''
inpt = [15, 22, 13, 27, 12, 10, 20, 25]


# 리스트 첫 원소를 계속 피버값으로 설정
# 순방(i)과 역방(j)으로 탐색하면서 각각 피버값보다 작지 않거나, 크지 않으면
# 반복문을 빠져나와 둘을 서로 바꾸고 다시 반복
# 모든 교환이 끝난 상태라면 피버값만 정렬이 안 되어 있을 거임
def partition(low, high) :
    pivotitem = inpt[low]
    pivotpoint = 0
    i = low + 1
    j = high-1

    # 역방과 순방이 마주쳤다면 이미 피버값 빼고 정렬이 되어 있다는 의미
    while i < j :
        while i < j and inpt[i] < pivotitem :
            i += 1
        while i < j and inpt[j] > pivotitem :
            j -= 1
        if i < j :
            temp = inpt[i]
            inpt[i] = inpt[j]
            inpt[j] = temp
            i += 1
            j -= 1

    # 여기까지 왔다면 피버값 빼고 모두 정렬된 상태
    pivotpoint = j
    # j = i-1
    temp = inpt[low]
    inpt[low] = inpt[pivotpoint]
    inpt[pivotpoint] = temp

    return pivotpoint
            
    

## divide
def quickSort(low, high) :
    pivotpoint = 0
    ## high 가 low보다 크다는 것은 대상이 2개 이상이라는 의미 
    if (low < high) :
        pivotpoint = partition(low, high)
        quickSort(low, pivotpoint-1)
        quickSort(pivotpoint+1, high)

# conquer은 없음 
def main() :
    quickSort(0, len(inpt)-1)

    print(inpt)


main()
