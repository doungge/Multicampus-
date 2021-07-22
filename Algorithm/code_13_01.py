##이진검색 일단 정렬을 하고 반으로 나누어가면서 검색하는 검색법 중요한 코드

##함수
def binSearch(ary, fdata):
    pos = -1
    start = 0
    end = len(ary)-1
    while(start <=end):
        mid =(start+end) // 2
        if(fdata == ary[mid]):
            return mid
        elif  fdata >ary[mid] :
            start = mid +1
        else:
            end = mid-1



    return pos
##전역
dataAry = [50,60,105,120,150,162,170,175,180,183,190]
findData = 170
##메인
print('배열 --->', dataAry)
position = binSearch(dataAry, findData)
if position == -1:  #없는 것을 표현할때는 -1이 관례이다.
    print('없다..')
else:
    print(findData, '는', position, '위치에 있음')