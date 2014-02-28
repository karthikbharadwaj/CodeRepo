__author__ = 'Karthik'

class Stack:

    def __init__(self):

        self._data = []
        self._min_element = None


    def _add(self,data):

        self._data.append(data)

        if data < self._min_element:

            self._min_element = data
        return



    def _pop(self,data):
        if self._is_empty()==1:
            raise "Stack error"
        self._data.pop()

    def _is_empty(self):

        if len(self._data) == 0:
            print "Stack is empty"
            return 1
        return 0

    def find_min(self):

