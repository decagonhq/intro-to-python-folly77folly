def divide(numb1,numb2,floor=True):
    try:
        first_Number=(numb1)
        second_Number=(numb2)
        if floor==True:
            print (first_Number//second_Number)
        else:
            print (first_Number/second_Number)        
    except TypeError as e:
        print(e)