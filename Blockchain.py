import hashlib
import datetime

class Block:
    
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash(data)
        
    def __repr__(self):
        return  'Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)
    
    def _calc_hash(self, hash_str):
        sha = hashlib.sha256()
        hash_str = hash_str.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()
    
class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def put(self, data):
        if self.tail is None:
            block = Block(data, None)
            self.head = self.tail = block
        else:
            self.tail = Block(data, self.tail) 
            
    def search(self, data):
        curr_block = self.tail
        while curr_block:
            if curr_block.data == data:
                return curr_block
            curr_block = curr_block.previous_hash
        
        return ValueError("Data not found in the blockchain.")
    
    def to_list(self):
        blockchain_list = list()
        curr_block = self.tail
        while curr_block:
            blockchain_list.append([curr_block.data, curr_block.timestamp, curr_block.hash])
            curr_block = curr_block.previous_hash
            
        return blockchain_list
        
bc = Blockchain()
bc.put('Previous Balance: 50 | cash flow: +25 | Current Balance: 75')
bc.put('Previous Balance: 75 | cash flow: +15 | Current Balance: 90')
bc.put('Previous Balance: 90 | cash flow: -10 | Current Balance: 80')
bc.put('Previous Balance: 80 | cash flow: -20 | Current Balance: 60')
print("The head of Blockchain: {}\n".format(bc.head))
print("The tail of Blockchain: {}\n".format(bc.tail))
print(bc.to_list())
