import sys
from queue import PriorityQueue

class Huffman_node(object):
    def __init__(self, freq, char = None, left = None, right = None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return other.freq > self.freq
    
    def __eq__(self, other):
        return other.freq == self.freq
    
    def __gt__(self, other):
        return other.freq < self.freq
    
def count_fr(data):
    frequencies = {}
    for char in data:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] +=1  
    return frequencies

def build_queue(frequencies):
    q = PriorityQueue()
    for value, fr in frequencies.items():
        node = Huffman_node(fr, value)
        q.put(node)
    return q
def merge(q):
    while q.qsize() > 1:
        l,r = q.get(), q.get()
        node = Huffman_node(l.freq+r.freq, None,l,r)
        q.put(node)    
    tree = q.get()
    
    return tree
def huffman_encoding(data):
    if len(data) == 0:
        return "", None
    
    # caculate frequency
    frequencies = count_fr(data)
    # built queue
    q = build_queue(frequencies)
    # merge
    tree = merge(q)
    
    # encode   
    encoded_value = dict()
    def traversal(head, code):
        if head.char is not None:
            encoded_value[head.char] = code
            return
        else:
            traversal(head.left, code+"0")
            traversal(head.right, code+"1")
    traversal(tree, "")
    
    # if there is only one type of character in data, encode 0
    if len(encoded_value) == 1:
        for value in frequencies:
            encoded_value[value] = "0"
        
    # final step
    encoded_data = ""
    for char in data:
        encoded_data = encoded_data + encoded_value[char]
        
    return encoded_data, tree

def huffman_decoding(encoded_data, tree):
    decoded_data = ""
    head = tree
    for bit in encoded_data:
        if bit == "0":
            if head.left is not None:
                head = head.left
        if bit == "1":
            if head.right is not None:
                head = head.right           
        if type(head.char) == str:
            decoded_data = decoded_data + head.char
            head = tree
            
    return decoded_data
    

if __name__ == "__main__":
    codes = {}

    # test case 1
    print("Test Case 1:")
    a_great_sentence1 = "The bird is the word"
    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence1)))
    print ("The content of the data is: {}".format(a_great_sentence1))
    encoded_data1, tree1 = huffman_encoding(a_great_sentence1)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data1, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data1))
    decoded_data1 = huffman_decoding(encoded_data1, tree1)
    print ("The content of the decoded data is: {}".format(decoded_data1))
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data1)))
    
    # test case 2
    print("Test Case 2:")
    a_great_sentence2 = "hhhhhhhhhh"
    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence2)))
    print ("The content of the data is: {}".format(a_great_sentence2))
    encoded_data2, tree2 = huffman_encoding(a_great_sentence2)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data2, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data2))
    decoded_data2 = huffman_decoding(encoded_data2, tree2)
    print ("The content of the decoded data is: {}".format(decoded_data2))
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data2)))
