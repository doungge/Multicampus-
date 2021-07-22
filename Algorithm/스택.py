#자료구조
## 선형 : 선형 리스트, 연결 리스트, 스택, 큐, 원형 큐
## 비선형 : 트리(이진 검색 트리), 그래프(인접행렬*)

#알고리즘
## 재귀, 정렬(선택정렬), 검색(이진검색)
## 함수
def isStackFull() : # 스택 꽉 확인
    global SIZE, stack, top
    if (top == SIZE-1) :
        return True
    else :
        return False

def push(data) : # 푸쉬
    global SIZE, stack, top
    if (isStackFull() == True) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if(top == -1):
        return True
    else : 
        return False

def pop(): 
    global SIZE, stack, top
    if(isStackEmpty()):
        print('스택이 비었다.')
        return None
    data = stack[top]
    stack[top] = None
    top -=1
    return data

def peek(): #다음에 무엇이 있는 지 확인
    global SIZE, stack, top
    if(isStackEmpty()):
        print('스택이 비었다.')
        return None
    return stack[top]

## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1 ## 스택이 비어있음을 뜻함

## 메인
push('커피1');push('커피2')

print( '바닥 |', stack)
retData = peek()
print('다음에 나올 것 --->', retData)
retData = pop()
print('빼낸 것 -->', retData)
retData = pop()
print('빼낸 것 -->', retData)
print( '바닥 |', stack)