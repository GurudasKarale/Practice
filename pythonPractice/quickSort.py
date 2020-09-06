def partition(a,low,high):
    pivot=a[high]              #consider last element as the pivot
    i=low-1                     #smallest element's index
    for j in range(low,high):
        if a[j]<pivot:           #check if current value is smaller than pivot
            i += 1                #increment i
            a[i],a[j]=a[j],a[i]   #swap a[i] and current value

    a[i+1],a[high]=a[high],a[i+1]
    return (i+1)                   #return the index of pivot
def quicksort(a,low,high):

    if low <high:                             #terminating condition
        pi=partition(a,low,high)              #partition the array
        quicksort(a,low,pi-1)                 #go on pushing the values in the call stack until it reaches the terminating condition and start popping the values i.e return back to the calling function
        quicksort(a,pi+1,high)

a=[3,2,5,7,9,4,6,12,10,45,34,23]
quicksort(a,0,len(a)-1)
print(a)

