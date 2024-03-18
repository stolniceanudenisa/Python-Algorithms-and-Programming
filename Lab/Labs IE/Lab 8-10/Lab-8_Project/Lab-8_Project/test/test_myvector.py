'''
Created on Nov 17, 2020

@author: Sergiu Ciubotariu
'''

from domain.myvector import MyVector

def test_create():
    v = MyVector("test_name", 'y', 1, [5,10,20])
    
    assert v.get_name_id() == "test_name"
    assert v.get_colour() == 'y'
    assert v.get_type() == 1
    assert v.get_values() == [5,10,20]
    
    v.set_name_id(1337)
    assert v.get_name_id() == 1337
    
    v.set_colour('m')
    assert v.get_colour() == 'm'
    
    v.set_type(2)
    assert v.get_type() == 2
    
    v.set_values([3,9,27])
    assert v.get_values() == [3,9,27]
    
