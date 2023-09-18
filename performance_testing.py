from linkedlist import LinkedList
from hashtable import HashTable
import sys
import timeit
import random

"""testing append methods for linked list and hashtable"""
def create_linked_list(iterations):
    linked_list = LinkedList()
    for _ in range(iterations):
        linked_list.append(_)
    # print('head: {}'.format(linked_list.head))
    # print('tail: {}'.format(linked_list.tail))
    return linked_list

def create_hashtable(iterations, buckets=8):
    hashtable = HashTable(buckets)
    for _ in range(iterations):
        hashtable.set(_, _)
    return hashtable


def test_ll_creation(length):
    print(f"Testing average creation time of LL with {length} items:")
    start = timeit.default_timer()
    for _ in range(1000):
        ll = create_linked_list(length)
    end = timeit.default_timer()
    return f"Time to run {(end - start)/1000} seconds per iteration on average\n"

def test_ll_find(linked_list, length):
    print(f"Testing average seek time in LL with {length} items:")
    start = timeit.default_timer()
    for _ in range (1000):
        item = random.randint(0, length-1)
        linked_list.find(item)
    end = timeit.default_timer()
    return f"Time to run {(end - start)/1000} seconds per iteration on average\n"

def test_ht_creation(items, buckets=8):
    print(f"Testing average creation time of Hash Table with {items} items in {buckets} buckets:")
    start = timeit.default_timer()
    create_hashtable(items, buckets)
    end = timeit.default_timer()
    return f"Time to run {(end - start)/1000} seconds per iteration on average\n"

def test_ht_find(hashtable, items):
    print(f"Testing average seek time in HT with {items} items:")
    start = timeit.default_timer()
    for _ in range (1000):
        key = random.randint(0, items-1)
        hashtable.get(key)
    end = timeit.default_timer()
    return f"Time to run {(end - start)/1000} seconds per iteration on average\n"

"""Test creation times of linked lists of varying lengths"""
print(test_ll_creation(100))
print(test_ll_creation(1000))
print(test_ll_creation(10000))

"""Test seek times of linked lists of varying lengths"""
length = 100
ll = create_linked_list(length)
print(test_ll_find(ll, length))

length = 1000
ll = create_linked_list(length)
print(test_ll_find(ll, length))

length = 10000
ll = create_linked_list(length)
print(test_ll_find(ll, length))

"""Test creation times of hashtables with varying numbers of items and bucket-list lengths"""
print(test_ht_creation(100, 5))
print(test_ht_creation(100, 10))
print(test_ht_creation(100, 20))
print(test_ht_creation(1000, 5))
print(test_ht_creation(1000, 10))
print(test_ht_creation(1000, 20))
print(test_ht_creation(10000, 5))
print(test_ht_creation(10000, 10))
print(test_ht_creation(10000, 20))

"""Test seek times of hashtables with varying numbers of items and bucket-list lengths"""
items = 100
buckets = 5
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))

items = 100
buckets = 10
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))

items = 100
buckets = 20
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))

items = 1000
buckets = 5
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))

items = 1000
buckets = 10
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))

items = 1000
buckets = 20
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))

items = 10000
buckets = 5
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))

items = 10000
buckets = 10
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))

items = 10000
buckets = 20
ht = create_hashtable(items, buckets)
print(test_ht_find(ht, items))




