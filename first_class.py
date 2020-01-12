class FirstClass:
    mean = 0.0
    median = 0.0
    mode = 0.0
    
    #calculates the mean of a list
    @staticmethod
    def calc_mean(numbs):
        FirstClass.mean = round( sum(numbs) / len(numbs), 2)
        # return FirstClass.mean


    @classmethod
    def calc_median(cls, numbs):
        numbs.sort()
        num_index = len(numbs) // 2
        if len(numbs) % 2 != 0:
            FirstClass.median = numbs[num_index]
            return
        print(sum(numbs[num_index - 1:num_index + 1]) / 2)
        FirstClass.median=sum(numbs[num_index - 1:num_index + 1]) / 2
        
    def calc_mode(self,numbs):
        set_of_numbs = list(set(numbs))
        highest_count = numbs.count(numbs[0])
        highest_mode = set_of_numbs[0]
        for i in range(1,len(set_of_numbs)):
            count_of_numbers = numbs.count(set_of_numbs[i])
            if count_of_numbers > highest_count:
                highest_count = count_of_numbers
                highest_mode = set_of_numbs[i]
        FirstClass.mode = highest_mode

mylist = [1, 2, 3, 4, 1, 1, 3, 3, 3]
score = FirstClass()
score.calc_mean(mylist)
score.calc_median(mylist)
score.calc_mode(mylist)
print(score.mean)
print(score.median)
print(score.mode)

