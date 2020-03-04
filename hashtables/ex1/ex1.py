#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

ht = HashTable(16)
hash_table_insert(ht, 10, 2)
print(ht)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    """
    YOUR CODE HERE
    """
    for i in weights:
        hash_table_insert(ht, i, limit-i)
        print(ht)
    for key in ht:
        hash_table_retrieve(ht, key)
        if key + checker == limit:
            if ht[key] > checker[key]:
                answer = (ht[key], checker[key])
            else:
                answer = (checker[key], ht[key])
            print(answer)
            

    return answer

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
