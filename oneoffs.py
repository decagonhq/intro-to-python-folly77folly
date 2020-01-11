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
        return('Only Numbers are Allowed')
    except Exception as e:
        return('Something is Wrong')

# print(divide(1,2))

# this function prints all weekdays and date
def days_of_week(*week, **date_of_release):
    for day in week:
        date_string=date_of_release['day'] + '-'+ date_of_release['month'] +'-'+ date_of_release['year']
        print (day, date_string)

days_of_week('monday','tuesday','wednesday','thursday','friday',year='2012',month='10',day='01')
