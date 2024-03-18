'''
Created on Nov 17, 2020

@author: Sergiu Ciubotariu
'''

class MyVector():
    
    def __init__(self, name_id, colour, new_type, values):
        '''
        Constructor
        '''
        self.__name_id = name_id
        self.__colour = colour
        self.__type = new_type
        self.__values = values
    
    def set_name_id(self, name_id):
        '''
        Setter for name_id
        '''
        self.__name_id = []
        self.__name_id = name_id

    def get_name_id(self):
        '''
        Getter for name_id
        '''
        return self.__name_id
    
    def set_colour(self, colour):
        '''
        Setter for colour
        '''
        self.__colour = colour

    def get_colour(self):
        '''
        Getter for colour
        '''
        return self.__colour
    
    def set_type(self, new_type):
        '''
        Setter for type
        '''
        self.__type = new_type

    def get_type(self):
        '''
        Getter for type
        '''
        return self.__type
    
    def set_values(self, values):
        '''
        Setter for values
        '''
        self.__values = values

    def get_values(self):
        '''
        Getter for values
        '''
        return self.__values
    
    def __str__(self):
        '''
        Print function
        '''
        return "Vector ID is: " + str(self.__name_id) + " with the colour: " + str(self.__colour) + ", type: " + str(self.__type) + " and the values: " + str(self.__values)
        
    def addScalarToVector(self, scalar):
        '''
        adds a scalar to the values of the vector
        Input: scalar - the scalar
        '''
        for i in range(len(self.__values)):
            self.__values[i] += scalar 
    
    def sumOfElements(self):
        '''
        Returns the sum of elements of the values of the vector
        '''
        k = 0
        for elem in self.__values:
            k += elem
        return k
    
    def productOfElements(self):
        '''
        Returns the product of elements of the values of the vector
        '''
        k = 1
        for elem in self.__values:
            k *= elem
        return k
    
    def averageOfElements(self):
        '''
        Returns the average of elements of the values of the vector
        '''
        k = 0
        vector_sum = 0
        for elem in self.__values:
            vector_sum += elem
            k += 1
        return vector_sum/k
    
    def minOfAVector(self):
        '''
        Returns the minimum of elements of the values of the vector
        '''
        vec_min = self.__values[0]
        for elem in self.__values:
            if elem < vec_min:
                vec_min = elem
        return vec_min
    
    def maxOfAVector(self):
        '''
        Returns the maximum of elements of the values of the vector
        '''
        vec_max = self.__values[0]
        for elem in self.__values:
            if elem > vec_max:
                vec_max = elem
        return vec_max 
    
    def addVectorToVector(self, vector):
        '''
        Adds the values of a vector to this vector
        Input: vector - an object of the type MyVector
        '''
        new_list = vector.get_values()
        for i in range (3):
            new_list[i] = new_list[i] + self.__values[i]
        self.set_values(new_list)
    
    def substractVectorFromVector(self, vector):
        '''
        Substracts from this vector the values of a given vector
        Input: vector - an object of the type MyVector
        '''
        new_list = vector.get_values()
        for i in range (3):
            new_list[i] = new_list[i] - self.__values[i]
        for i in range (3):
            new_list[i] = -new_list[i] 
        self.set_values(new_list)
    
    def multiplicationVectorWithVector(self, vector):
        '''
        Multiplies the 2 vectors
        Input: vector - an object of the type MyVector
        '''
        new_list = vector.get_values()
        k = 0
        for i in range (3):
            new_list[i] = new_list[i] * self.__values[i]
            k += new_list[i]
        self.set_values(new_list)
        return k
    
    
    
    
    
    
    
    
    
    
    
    
    