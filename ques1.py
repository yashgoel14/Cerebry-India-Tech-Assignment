# some assumptions which I have considered after reading the question
#
# 1) For every element in the list it is sure that error is there otherwise I have to add one more condition such as 
#     elif mp.get(i):
#         mp[i]-= 1
#
# 2) The length of both arrays will be same and both arrays will always consist some element

def resolveError(arr1,e,arr2):
    check = True
    mp = {}
    for ele in arr2:
        if ele in mp:
            mp[ele]+=1
        else:
            mp[ele]=1

    for i in arr1:
        if mp.get(i-e):
            mp[i-e]-= 1
        elif mp.get(i+e):
            mp[i+e]-= 1
        else:
            check = False
            break
    if check:
        print(mp)
        return True
    else:
        return False

A = list(map(int,input().split()))
E = int(input())
B = list(map(int,input().split()))

if len(A)==len(B):
    print(resolveError(A,E,B))
else:
    print("False")

# Time complexity: O(n)
# Space complexity: O(n)