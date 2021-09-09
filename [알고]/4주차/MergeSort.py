'''
MergeSort Algorithm
'''

# for merge
def merge(f, b, U, V, inPt) :
    i, j , k = 0, 0, 0

    # U나 V 둘 중 하나라도 소진되면 루프 탈출
    # U와 V 값 순서대로 비교해서 오리지널에 복사
    while(i < f and j < b) :
        if (U[i] < V[j]) :
            inPt[k] = U[i]
            i += 1
        else :
            inPt[k] = V[j]
            j += 1
        k += 1

    ## 루프에서 탈출하였다면,##
    # 어느 한 쪽 원소가 남아있거나 둘 다 없을 경우
    if i < f :
        for n in range(i, f) :
            inPt[k] = U[n]
            k += 1
    elif j < b :
        for n in range(j, b) :
            inPt[k] = V[n]
            k += 1

    
## for divide
def mergeSort(n, inPt) :
    
    if n > 1 :
        f = n//2
        b = n-f

        U, V = [], []

        ## copy U, V for S in half (divide) ##
        for i in range(f) :
            U.append(inPt[i])
        for i in range(b, n) :
            V.append(inPt[i])

        ## Recursion of divided input ##
        mergeSort(f, U)
        mergeSort(b, V)

        # Conquer the divided inputs into original
        merge(f, b, U, V, inPt)
        

def main() :
    inPt = [27, 10, 12, 20, 25, 13 , 15, 22]

    mergeSort(len(inPt), inPt)

    print(inPt)


main()
