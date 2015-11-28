def quicksort():
    inputquick = raw_input("Example input:");
    a= map(int,inputquick.split())
    if len(a)>100:
        print "input Over 100"
        return
    fsort=sort(a)
    fsort=' '.join(map(str,fsort))
    print "Example output:",fsort
    return 
def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)  
    else:  
        return array
quicksort()
