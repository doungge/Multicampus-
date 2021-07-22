##재귀함수

## 함수
def openBox():
    global count
    print('박스 열기 ~~~')
    count-=1
    if count==0:
        print("## 박스에 선물 넣기 ##")
        return  #방금 부른 함수로 돌아간다.

    openBox() #자기 자신을 재호출 하는 것 제한조건이 필요하다.
    print('박스 닫기!!')
## 변수
count  = 10

## 메인
openBox()