class TreeNode() : # 트리노드의 틀 (붕어빵 기계)
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무','에이핑크', '걸스데이', '트와이스']

#첫노드 생성(약간 다름)
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(root)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True: #몇번 비교해야 자리잡을지 모름
        if name <current.data :
            if current.left == None: #왼쪽에 자리가 남았는지 확인    
                current.left = node
                break #while문을 나가는 것
            current = current.left

        else : 
            if current.right == None: #왼쪽에 자리가 남았는지 확인    
                current.right = node
                break #while문을 나가는 것
            current = current.right

    memory.append(node)

print('이진 탐색 트리! 구성 완료')

##데이터를 검색(=탐색)할 때 완전 효율적
findName = '바마무'

current = root
while True:
    if (current.data == findName):
        print(findName, '찾았당~~')
        break
    elif(findName<current.data):
        if current.left ==None :
            print('없음')
            break
        current = current.left
    else:
        if current.right ==None:
            print('없음')
            break
        current=current.right