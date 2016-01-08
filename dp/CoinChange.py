# ???? explain this solution
def cc(arr,m,n):
    table = [0]*(n+1)
    table[0] = 1

    for i in xrange(m):
        print 
        for j in xrange(arr[i],n+1):
            table[j] += table[j-arr[i]]
            print table[j], j,arr[i],table[j-arr[i]], table


    return table[n]

# # Dynamic Programming Python implementation of Coin Change problem
# def count(S, m, n):
#     # We need n+1 rows as the table is consturcted in bottom up
#     # manner using the base case 0 value case (n = 0)
#     table = [[0 for x in range(m)] for x in range(n+1)]
#     # Fill the enteries for 0 value case (n = 0)
#     for i in range(m):
#         table[0][i] = 1
#     # Fill rest of the table enteries in bottom up manner
#     for i in range(1, n+1):
#         for j in range(m):
#             # Count of solutions including S[j]
#             x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
#             # Count of solutions excluding S[j]
#             y = table[i][j-1] if j >= 1 else 0
 
#             # total count
#             table[i][j] = x + y
#             print table, i,j,x,y
#     return table[n][m-1]
 
# # Driver program to test above function
# arr = [1, 2, 3]
# m = len(arr)
# n = 4
# print(count(arr, m, n))
 
# This code is contributed by Bhavya Jain


# arr = [1, 2, 3]
# m = len(arr)
# n = 4
# print(cc(arr, m, n))
# my backtracking solution O(n)
# def cc(arr,n):
#     res = []
#     subres = []
#     cc2(arr,n,res,subres)
#     return res


# def cc2(arr,n,res,subres):
#     if n == 0:
#         res.append([j for j in subres])
#         return
#     elif n < 0:
#         return
#     else:
#         for i in arr:
#             if not subres:
#                 cc2(arr,n-i,res,subres+[i])
#             elif i >= subres[-1]:
#                 cc2(arr,n-i,res,subres+[i]) 


arr = [1, 2, 3]
m = len(arr)
n = 4
cc(arr, m,n)
 


# arr = [1, 2, 3]
# m = len(arr)
# n = 4
# print(cc(arr, m, n))
