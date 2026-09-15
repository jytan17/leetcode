from typing import List, Optional


class Node:
    def __init__(self, key=None, val=None) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        out = self.hash_map.get(key)

        if out:
            nxt, prev = out.next, out.prev
            nxt.prev = prev
            prev.next = nxt

            second = self.head.next
            self.head.next, out.prev = out, self.head
            out.next = second
            second.prev = out

        return out.val if out else -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].val = value
            self.get(key)
            return

        new_node = Node(key, value)
        self.hash_map[key] = new_node

        second = self.head.next
        new_node.next = second
        second.prev = new_node

        self.head.next = new_node
        new_node.prev = self.head

        if len(self.hash_map) > self.capacity:
            cur_last = self.tail.prev
            new_last = cur_last.prev
            new_last.next = self.tail
            self.tail.prev = new_last
            del self.hash_map[cur_last.key]
