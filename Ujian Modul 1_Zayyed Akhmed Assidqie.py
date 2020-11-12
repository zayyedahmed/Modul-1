# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 09:24:58 2020
Using Spyder

@author: Akhmed
"""



#Nomor 1
def nomortelepon(nomor) :
    def validate(input_list):
        valid = True
        for i in input_list:
            if type(i) != int:
                valid = False
                if i in  ["@","!","#","$","%","^","&","+"]:
                    print("Invalid Input, No Symbols")
                    return valid
                elif type(i) == str:
                    print("Invalid Input, No. Alphabet")
                    return valid
        return valid
    is_valid = validate(nomor)
    if not is_valid :
        return
    a = 0
    for i in nomor :
        if type(i) == int :
            a += 1
        if i > 9 or i < 0  :
            a += 1
    if a!=len(nomor) :
        return 'Input only positive number'
    elif len(nomor) == 10 :
        abc = '('
        for i in range(0,3) :
            abc += (str(nomor[i]))
        abc += ') '
        for i in range(3,6) :
            abc += (str(nomor[i]))
        abc += '-'
        for i in range(6,len(nomor)) :
            abc += (str(nomor[i]))        
        return abc
    else :
        return 'Digits must be in length of 10, not more or less'
print(nomortelepon([0,1,2,3,4,5,6,7,8,9]))


#NOMOR 2
arr = [False, 1, 0, 1, 2, 0, 1, 3, '@']
def moveZeros(arr):
  hasil = []
  Count = 0
  for index in range(0, len(arr)):
    if arr[index] != 0 or type(arr[index]) == bool:
      hasil.append(arr[index])
    else:
      Count += 1
  
  for count in range(0, Count):
    hasil.append(0)
    
  print ("MoveZero ", arr)  
  print ('result: ', hasil)     
moveZeros(arr)


#NOMOR 3
arr1 = [30, 1,2,3,4,5, 20, 7]
arr2 = [12, 10,10,10,10]
class Statistic:
  def mean(self, input_list):
    valid = self._validate(input_list)
    if not valid:
      self._falseReturn()
    else:
      sum = 0
      for item in input_list:
        sum += item
      mean = sum / float(len(input_list))
      print ('st.mean: ', mean)

  def median(self, input_list):
    valid = self._validate(input_list)
    if not valid:
      self._falseReturn()
    else:
      input_list.sort()
      list_len = len(input_list)
      median_index = (list_len - 1) // 2
      median = 0
      if (list_len % 2):
        median = input_list[median_index]
      else:
        median = (input_list[median_index] + input_list[median_index + 1])/2.0
      print ('st.median: ', median)
  #def modus(self, input_list):
    #valid = self._validate(input_list)
    #if not valid:
      #self._falseReturn()
    #else:
      #input_list.sort()
      #list_len = len(input_list)
      
  def _validate(self, input_list):
    valid = True
    for item in input_list:
      if type(item) != int:
        valid = False
    return valid

  def _falseReturn(self):
    print ('Invalid input, all values must be integer')
  
st = Statistic()

st.mean(arr2)
st.median(arr2)













