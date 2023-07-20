def MatrixProduct(array,row,b):
    col=len(array[0])
    for i in range(row):
        for j in range(col):
            array[i][j]*=b
    return array

if __name__ == '__main__':
    array=[]
    row=int(input())
    for i in range(row):
        col=list(map(int,input().split()))
        array.append(col)
    b=int(input())
    print(*MatrixProduct(array,row,b))
"""
Matrix Product
You are given a matrix A and and an integer B, 
you have to perform scalar multiplication of matrix A with an integer B.
"""