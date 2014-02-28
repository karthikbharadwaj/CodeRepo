__author__ = 'Karthik'


class LinkNode:

    def __init__(self, data):
        self._data = data
        self._next = None
        return


class LinkList():

    def __init__(self):
        self._head = None

    def _add_node(self, data):

        new_node = LinkNode(data)

        if self._head is None:

            self._head = new_node
        else:
            current = self._head

            while current._next is not None:
                current = current._next

            current._next = new_node

    def _print_nodes(self):

        if self._head is None:
            print "List is empty"
            return
        else:
            current = self._head

            while current is not None:
                print current._data
                current = current._next

    def _remove_node(self, data):

        current = self._head

        if self._head._data == data:
            return self._head._next

        else:

            while current._next is not None:

                if current._next._data == data:

                    current._next = current._next._next
                    return self._head

    def _remove_duplicates(self):

        if self._head is None:
            return

        previous = self._head
        current = previous._next

        while current is not None:
            runner = current._next
            while runner is not None:
                if current._data == runner._data and current != runner:

                    previous._next = current._next
                    current = current._next

                runner = runner._next

            previous = current
            current = current._next

        return

    def _find_mth_element(self, m):
        first = self._head
        second = self._head
        counter = m
        while second is not None:

            second = second._next

            counter -= 1

        if counter > 0:
            print "Less than m elements"
            return -1

        while second is not None:

            second = second._next
            first = first._next

        return first

    def _find_palindrome(self):

        first = self._head
        current = self._head


link_list = LinkList()

link_list._add_node(14)
link_list._add_node(4)
link_list._add_node(6)
link_list._add_node(5)
link_list._add_node(4)

#link_list._remove_duplicates()
first = link_list._find_mth_element(3)
link_list._print_nodes()
