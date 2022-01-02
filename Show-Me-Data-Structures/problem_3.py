
import heapq
from collections import Counter
import sys
class Tree:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right
#defining a less than funtion
    def __lt__(self, other):
        return self.freq < other.freq
    

def our_tree(text):
    counter = Counter(text)
    priority_q = [Tree(ch, counter[ch]) for ch in counter]
    heapq.heapify(priority_q)
    while len(priority_q) > 1:
        left = heapq.heappop(priority_q)
        right = heapq.heappop(priority_q)
        parent = Tree(None, left.freq+right.freq, left, right)
        heapq.heappush(priority_q, parent)
    return heapq.heappop(priority_q)


def our_map(root):
    def depth_first_search(root, code, encoding_map):
        if root.ch:
            encoding_map[root.ch] = ''.join(code)
        else:
            code.append('0')
            depth_first_search(root.left, code, encoding_map)
            code.pop()
            code.append('1')
            depth_first_search(root.right, code, encoding_map)
            code.pop()
    encoding_map = {}
    depth_first_search(root, [], encoding_map)
    return encoding_map


def huffman_encoding(text_input):
    root = our_tree(text_input)
    encoding_map = our_map(root)
    return ''.join([encoding_map[ch] for ch in text_input])


def huffman_decoding(encoded_data, root):
    if root.ch:
        return root.ch * len(encoded_data)
    decoded_data = []
    node = root
    for x in encoded_data:
        if x == "0":
            node = node.left
        else:
            node = node.right
        if node.ch:
            decoded_data.append(node.ch)
            node = root
    return ''.join(decoded_data)

 


a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data= huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, our_tree(a_great_sentence))

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data)cod)