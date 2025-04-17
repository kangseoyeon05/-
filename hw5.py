def read_single_digit(msg):
    if msg==1:
        return '일'
    elif msg==2:
        return '이'
    elif msg==3:
        return '삼'
    elif msg==4:
        return '사'
    elif msg==5:
        return '오'
    elif msg==6:
        return '육'
    elif msg==7:
        return '칠'
    elif msg==8:
        return '팔'
    elif msg==9:
        return '구'
    else:
        return '영'
def read_number(number):
    h= number // 100
    t = (number % 100) // 10
    o = number % 10
    print(read_single_digit(h), end=' ')
    print(read_single_digit(t), end=' ')
    print(read_single_digit(o), end=' ')
num = int(input("세 자리 정수 입력: "))
read_number(num)

    
    

   
    
    





        
            
