import numpy as np
a=np.random.randint(2,100,(5,5))
print(a)
k=a[2,2]
print(f'middle elemnt of the array is {k}')
b=np.mean(a[0,:])
c=np.mean(a[1,:])
d=np.mean(a[2,:])
e=np.mean(a[3,:])
f=np.mean(a[4,:])
print(f'the mean for each of the rows are {b},{c},{d},{e},{f}')
mean=np.mean(a)
new_array=a[a>mean]
print(new_array)
def numpy_spiral_holder(matrix):
    spiral=[]
    while matrix.size>0:
        spiral.extend(matrix[0,:])
        matrix=matrix[1:,:]
        if matrix.size==0:
            break
        spiral.extend(matrix[:,-1])
        matrix=matrix[:,:-1]
        if matrix.size==0:
            break
        spiral.extend(matrix[-1,::-1])
        matrix=matrix[:-1,:]
        if matrix.size==0:
            break
        spiral.extend(matrix[::-1,0])
        matrix=matrix[:,1:]
    return spiral
spiral_order=numpy_spiral_holder(a)
print(spiral_order)





































































