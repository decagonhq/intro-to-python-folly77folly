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


def last_song(*song_title,**date_of_release):
    print(song_title)
    print(date_of_release)



songs_title=['wakeup','takehome']
date_of_release={'year': "2020", 'month': "01", 'day': "01"}
last_song(songs_title,date_of_release)