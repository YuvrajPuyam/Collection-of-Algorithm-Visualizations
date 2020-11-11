import time

def merge_sort(data, drawData, tick):
    merge_sort_alg(data,0,len(data)-1,drawData,tick)


def merge_sort_alg(data,left, right, drawData, tick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data,left,middle, drawData,tick)
        merge_sort_alg(data,middle+1,right, drawData,tick)
        merge(data,left,middle,right, drawData,tick)

def merge(data,left,middle, right,drawData,tick):
    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < (len(leftPart)) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx+=1
            else: 
                data[dataIdx] = rightPart[rightIdx]
                rightIdx+=1    

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx+=1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx+=1            
    drawData(data,['green'if x == dataIdx or x==rightIdx or x == leftIdx else 'red' for x in range(len(data))])
    time.sleep(tick)
