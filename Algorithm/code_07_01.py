## 함수


## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1 
## 메인

##enQueue
rear += 1
queue[rear]='화사'

rear+=1
queue[rear]='솔라'

#deQueue
front +=1
retData = queue[front]
queue[front] = None
print('들어갈 손님 --->', retData)
front +=1
retData = queue[front]
queue[front] = None
print('들어갈 손님 --->', retData)
print('출구<---', queue,"<-------입구")