'''
Stooge Sort
'''
inpt = [15, 22, 13, 27, 12, 10, 20, 25]

def stoogeSort(low, high) :
    # high랑 low를 뺀 것이 2보다 작다는 것은 원소가 두 개 이하라는 뜻
    # 충분히 작을 때까지 분할된 것이므로 여기서 직접 계산
    if high - low - 2 < 0 :
        if inpt[low] > inpt[high] :
            # exchange s[low], s[high]
            temp = inpt[low]
            inpt[low] = inpt[high]
            inpt[high] = temp
    else :
        # 이제 충분히 작아질 때까지 분할해야 함.
        # stoogeSort는 전체 문제를 2/3으로 나누고 세 번 반복해야 함.

        # 전체 개수의 1/3 = k
        k = (high - low + 1) // 3
        stoogeSort(low, high - k)
        # print("1", inpt)
        stoogeSort(low + k, high)
        # print("2", inpt)
        stoogeSort(low, high - k)
        # print("3", inpt)
        

def main() :
    stoogeSort(0, len(inpt)-1)

    print(inpt)


main()
