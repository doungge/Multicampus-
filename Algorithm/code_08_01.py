## 함수
class TreeNode() : # 트리노드의 틀 (붕어빵 기계)
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
## 전역
## 메인
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

print(node1.data)
print(node1.left.data, node1.right.data)
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)