import collections

def read_list2():
    l = []
    n = int(input("Dati numarul de elemente al listei: "))
    for i in range(n):
        l = l + [int(input("Dati elementele din lista: "))]
    return l

def longest(a, n, k):
    freq = collections.defaultdict(int)

    start = 0
    end = 0
    now = 0
    l = 0
    for i in range(n):

        # mark the element visited
        freq[a[i]] += 1

        # if its visited first time, then increase
        # the counter of distinct elements by 1
        if (freq[a[i]] == 1):
            now += 1

        # When the counter of distinct elements
        # increases from k, then reduce it to k
        while (now > k):

            # from the left, reduce the number
            # of time of visit
            freq[a[l]] -= 1

            # if the reduced visited time element
            # is not present in further segment
            # then decrease the count of distinct
            # elements
            if (freq[a[l]] == 0):
                now -= 1

            # increase the subsegment mark
            l += 1

        # check length of longest sub-segment
        # when greater than previous best
        # then change it
        if (i - l + 1 >= end - start + 1):
            end = i
            start = l

    # print the longest sub-segment
    for i in range(start, end + 1):
        print(a[i], end=" ")

def main():
    l=[]
    l = read_list2()
    n = len(l)
    k = 3
    longest(l, n, k)

if __name__ == "__main__":
    main()
