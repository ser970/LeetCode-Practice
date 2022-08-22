import math
class Solution(object):
    def findMedianSortedArrays(self, array1, array2):
        n = math.ceil((len(array1)+len(array2))/2)
        if len(array1) == 0:
            if len(array2)%2==0:
                return((array2[(n-1)]+array2[n])/2)
            return(array2[(n-1)])
        if len(array2) == 0:
            if len(array1)%2==0:
                return((array1[(n-1)]+array1[n])/2)
            return(array1[(n-1)])
        if len(array1)>len(array2):
            return self.findMedianSortedArrays(array2,array1)
        high = len(array1)
        low = 0
        nth = get_n(array1,array2,n,high,low)
        if((len(array1)+len(array2))%2)==0:
            value1 = nth[0]
            if nth[1] == 0:
                next_val1 = nth[2]
                next_val2 = n-nth[2]
            else:
                next_val1 = n-nth[2]
                next_val2 = nth[2]
            if next_val1 >= len(array1):
                value2 = array2[next_val2]
            if next_val2 >= len(array2):
                value2 = array1[next_val1]
            if next_val1 < len(array1) and next_val2 < len(array2):
                value2 = min(array1[next_val1],array2[next_val2])
            output = (value1+value2)/2
        else:
            output = nth[0]
        return output

def get_n(array1,array2,n,high,low):
    num_vals1 = int(math.floor((high+low)/2))
    num_vals2 = n-num_vals1
    if(num_vals2>len(array2)):
        low = num_vals1+1
        return get_n(array1, array2, n, high, low)
    if(num_vals1==0):
        if array2[(num_vals2-1)] <= array1[0]:
            return (array2[(num_vals2-1)],1,num_vals2)
        low = num_vals1+1
        return get_n(array1, array2, n, high, low)
    if num_vals2==0:
        if array1[(num_vals1-1)] <= array2[0]:
            return (array1[(num_vals1-1)],0,num_vals1)
        high = num_vals1-1
        return get_n(array1, array2, n, high, low)
    test_val1 = array1[(num_vals1-1)]
    test_val2 = array2[(num_vals2-1)]
    if num_vals2 < len(array2):
        check_val1 = array2[num_vals2]
    else:
        check_val1 = test_val1+1
    if num_vals1 < len(array1):
        check_val2 = array1[num_vals1]
    else:
        check_val2 = test_val2+1
    if test_val1<=check_val1 and test_val2<=check_val2:
        if test_val1 >= test_val2:
            return (test_val1,0,num_vals1)
        return (test_val2,1,num_vals2)
    if test_val1 > check_val1:
        high = num_vals1-1
        return get_n(array1, array2, n, high, low)
    low = num_vals1+1
    return get_n(array1, array2, n, high, low)
        