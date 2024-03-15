class Utils:
    @staticmethod
    def __partition(list, start, end, key = lambda x:x, reverse = False):
        i = start - 1
        pivot = list[end]
        for j in range(start, end):
            if (reverse == True and key(list[j]) >= key(pivot)) or (reverse == False and key(list[j]) <= key(pivot)):
                i+=1
                list[i], list[j] = list[j], list[i]
        list[i+1], list[end] = list[end], list[i+1]
        return (i+1)

    @staticmethod
    def __quick_sort(list, start, end, key = lambda x:x, reverse = False ):
        if len(list) == 1:
            return list
        if start < end:
            pi = Utils.__partition(list, start, end, key, reverse)
            Utils.__quick_sort(list, start, pi -1, key, reverse)
            Utils.__quick_sort(list, pi + 1, end, key, reverse)

    @staticmethod
    def sort(list, key = lambda x: x, reverse = False):
        Utils.__quick_sort(list, 0, len(list) - 1, key, reverse)
        return list



