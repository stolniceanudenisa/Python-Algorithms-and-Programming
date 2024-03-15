import operator

a = [1,2,3,4,5]
size = len(a)

def p1(a):
    #returneaza lista oglindita
    #a.reverse()
    a = a[::-1]
    return a

print(p1(a))


def test_p1():
    assert p1([]) == []
    assert p1([1, 2, 5]) == [5, 2, 1]
    assert p1(["ana", "are", "mere"]) == ["mere", "are", "ana"]
    assert p1("roxana") == "anaxor"
    assert p1([1, [2,3], [4,5,6]]) == [[4,5,6], [2,3], 1]
    assert p1([1, "a", 5]) == [5, "a", 1]


test_p1()

a = [1,2,3,4,5]
b = ["a", "b", "c", "d","e"]
c =[1,"a", 2,"b", 3,"c", 4,"d", 5,"e"]


def p2(a,b):
    lista=[]
    for x,y in zip(a,b):
        lista.append(str(x)+y)
    return lista


def test_p2():
    assert p2([1,2,3],["unu", "doi", "trei"]) == ["1unu", "2doi", "3trei"]
    #assert p2([], [4,5,6]) == [4,5,6]


test_p2()


def p3(list, p):
    while p in list:
        list.remove(p)
    return list

print(p3([1,2,35,2,2,5,6,72,2,2,8],2))

def test_p3():
    assert p3([1,2,2,3,4], 2) == [1,3,4]
    assert p3([], 4) == []
    assert p3(["a", "a", "b"], "a") == ["b"]
    assert p3([1,3], 2) == [1,3]

test_p3()


def p4(lista):
    return tuple(lista)

#[1,2,3] = (1,2,3)

  #      0       1
dict = {"Key1":1,"Key2":2}
a = dict.items() #-> ("Key1", val1), ("Key2", val2)


def p5(dict):  #sortare de dictionar
    dict_out = sorted(dict.items(), Key=operator.itemgetter(1)) # dupa valoare


def test_p5():
    assert p5({1:2, 3:4, 4:3, 2:1, 0:0}) == {0:0, 2:1, 1:2, 4:3, 3:4}
    #00 12 21 34 43 (in functie de 0)


def p6(dict,Key,val) #schimbare/inlocuire valoare din dictionar de la cheia key
    for d in dict: #d ia doar cheia ///////// daca punem .items ia si valoarea -> se face tuplu
        if d == Key
            dict[Key] = val
            #{0:0, 1:2}
            #{0:9, 1:2}
    return dict

#val2 = dict[Key]
'''
    for d in dict.items():
        Key = d[0]
        val = d[1]
 '''

def test_p6():
    assert p6({1:1, 2:2},2 ,9) == {1:1, 2:9}       # la cheia 2 se schimba cu 9  /// schimbam valoarea de la cheia 2 cu 9