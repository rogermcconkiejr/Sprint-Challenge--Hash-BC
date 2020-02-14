#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    sortedHash = HashTable(length)
    """
    YOUR CODE HERE
    """
    for i in tickets:
        hash_table_insert(hashtable, i[0],i[1])
    first_flight = hash_table_retrieve(hashtable, None)
    hash_table_insert(sortedHash, first_flight[0], first_flight[1])
    for i in hashtable:
        if i[0] == i[]

