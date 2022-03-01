# Construct Binary Tree from Parent Array
# https://practice.geeksforgeeks.org/problems/construct-binary-tree-from-parent-array/1

'''
Approach: 
 Step 1:
The simple method to solve this problem is we just creat first an array of Node having value at nodes from 0 to N-1 because we know from the question is that the indexes of parent array is represent values of Node and the value of parent array is represent the parent Node having this value of the Node having value equal to the index. 

step 2: 
Now we have an array of Nodes of tree. so we will traverse the parent array and will check if parent[i] = -1 then mark arr[i] as root of tree. if arr[parent[i]].left or arr[parent[i]]->right is None then make arr[parent[i]].left or arr[parent[i]].right = arr[i] accordingly .

step 3: Now return the root of tree.

'''


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:
    def createTree(self, parent, N):
        arr = []
        root = None

        for i in range(N):
            arr.append(Node(i))

        for i in range(N):

            if(parent[i] == -1):
                root = arr[i]

            else:
                if(not arr[parent[i]].left):
                    arr[parent[i]].left = arr[i]

                elif(not arr[parent[i]].right):
                    arr[parent[i]].right = arr[i]

        return root
