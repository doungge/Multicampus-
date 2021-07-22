
#def addNumber(num):
#    if num<=1:
#        return 1

 #   return num+addNumber(num-1)

#print(addNumber(10))

def countDown(n):
    if(n==0):
        print("발사")
    else:
        print(n)
        countDown(n-1)

countDown(5)