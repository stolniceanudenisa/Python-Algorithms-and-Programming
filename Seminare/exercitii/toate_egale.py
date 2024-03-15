def subarray(arr, n):
    ans, temp = 1, 1

    # Traverse the array
    for i in range(1, n):

        # If element is same as previous
        # increment temp value
        if arr[i] == arr[i - 1]:
            temp = temp + 1
        else:
            ans = max(ans, temp)
            temp = 1

    ans = max(ans, temp)

    # Return the required answer
    return ans


def cea_mai_lunga_secv_care_are_toate_el_egale(lst):
    '''
    Determina cea mai lunga subsecventa care are toate elementele egale.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''
    n = len(lst)
    lc = 1
    rezultat=1
    for i in range(1,n):
        if lst[i]==lst[i-1]:
            lc=lc+1
        else:
            rezultat=max(rezultat,lc)
            lc=1
    rezultat = max(rezultat,lc)
    return rezultat



# Driver code
arr = [2, 2, 1, 1, 2,
       2, 2, 3, 3]
n = len(arr)

# Function call
print(subarray(arr, n))