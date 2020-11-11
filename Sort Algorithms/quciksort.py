import time

def partition(data,low,high,drawData,tick):
    i = low - 1
    pivot = data[high]

    for j in range(low,high):
        if data[j] < pivot:
            i = i+1
            data[i],data[j] = data[j],data[i]
            drawData(data,['green' if x==i or x==j else 'red' for x in range(len(data))])
            time.sleep(tick)

    data[i+1],data[high] = data[high],data[i+1]   
    drawData(data,['green' if x==i+1 or x==high else 'red' for x in range(len(data))])     
    return i+1

def quickSort(data,low,high,drawData,tick):
    if low<high:
        pi = partition(data,low,high,drawData,tick)
        quickSort(data,low,pi-1,drawData,tick)
        quickSort(data,pi+1,high,drawData,tick)
    

