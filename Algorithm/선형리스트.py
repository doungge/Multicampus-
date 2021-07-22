## 선형 리스트
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1):
        katok[i]=katok[i-1]
        katok[i-1] = None

    katok[position] = friend

def delete_data(position):
    kLen=len(katok)
    katok[position] = None
    for i in range(position +1, kLen,1):
        katok[i-1] = katok[i]
        katok[i]=None
    del(katok[kLen-1])
## 전역 부분
katok = []
select = -1

while (select != 4):
    select = int(input('선택(1추가, 2삽입,3삭제, 4종료 -->'))

    if (select  ==1):
        data = input('추가할 친구-->')
        add_data(data)
        print(katok)
    elif(select == 2):
        pos  = int(input('넣을 인덱스 값 -->'))
        data =  input('삽입할 친구 -->')
        insert_data(pos, data)
        print(katok)
    elif(select==3):
        pos = int(input('삭제할 친구 위치-->'))
        delete_data(pos)
        print(katok)
    elif(select == 4):
        pass
    else:
        print(" 잘못입력 ")
