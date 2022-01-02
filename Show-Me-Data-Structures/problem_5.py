
from datetime import datetime
import hashlib

class Block:
    
    def __init__(self, data, timestamp, previous_hash):
        
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        sha.update(data.encode('utf-8'))
        #sha.update(sha_str)
        return sha.hexdigest()

                   
                   
                   
class Blockchain:
    def __init__(self):
                   
        self.head = None

    def move_to_end(self, data):
        if self.head is None:
            block = Block(data,datetime.utcnow(), None)
            self.head = block

            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Block(data, datetime.utcnow(), node.hash)
        
        

some_blockchain = Blockchain()



some_blockchain.move_to_end('Data A')
some_blockchain.move_to_end('Data B')
some_blockchain.move_to_end('Data C')

a = some_blockchain.head
b = some_blockchain.head.next
c = some_blockchain.head.next.next


#  recreate blockchain from linked list

print('Block 0:')
print('Timestamp :', a.timestamp)
print('Data: ',a.data)
print('SHA256 Hash: ',a.hash)
print('Previous Hash: ', a.previous_hash)

print('Block 1:')
print('Timestamp :', b.timestamp)
print('Data: ',b.data)
print('SHA256 Hash: ',b.hash)
print('Previous Hash: ', b.previous_hash)

print('Block 2:')
print('Timestamp :', c.timestamp)
print('Data: ',c.data)
print('SHA256 Hash: ',c.hash)
print('Previous Hash: ', c.previous_hash)


#make sure  previous hash are correct

print(a.hash == b.previous_hash)

print(b.hash == c.previous_hash)