import random, sys
SEED = 8
random.seed(SEED)
NONWORD = "@" 

class Hashtable:
    """
    Class represents a hashtable that uses linear probing for collision
        handling. Size of table is passed into constructor.
    """
    def __init__(self, size):
        """
        Constructor
        Parameters: size (int) -> specifies size of table
        """
        self._pairs = [None] * size
        self._size = size

    def put(self, key, value):
        """
        Places the key and value in the table. Index is determined
            by the hash of the key. Uses linear probing.
        Parameters: key (str) -> key to be added
                    value (str) -> value to be added
        """
        index = self._hash(key)
        count = 0

        while self._pairs[index] is not  None and self._pairs[index][0] != key:
            if count > self._size:
                print("Hash table is full.")
                sys.exit(0)
            index = (index - 1) % self._size
            count += 1

        if self._pairs[index] is not None:
            self._pairs[index][1] += [value]
        else:
            self._pairs[index] = [key, [value]]
    
    def get(self, key):
        """
        Returns the value associated with the key
        Parameters: key (str) -> key to get value of
        Returns:    (str) -> value associated with key
        """
        index = self._hash(key)
        while self._pairs[index] != None:
            if self._pairs[index][0] == key:
                return self._pairs[index][1]
            index = (index - 1) % self._size
        return None
    
    def __contains__(self, key):
        """ Returns True if key is in the table, else False """
        index = self._hash(key)
        while self._pairs[index] != None:
            if self._pairs[index][0] == key:
                return True
            index = (index - 1) % self._size
        return False           

    def __str__(self):
        """ Returns the table as a string """
        return str(self._pairs)


    def _hash(self, key):
        """ hash function used for indexing """
        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size


def add_nonwords(words, prefix_len, table_len):
    """
    Essentially implements a queue with shifting
        to handle adding intial nonwords to dict
    Parameters: words(list) -> first line from file
                prefix_len(int) -> user entered prefix_len
                table_len(int)  -> size of table to create
    Returns:    HashTable -> markov chain table with nonword cases added

    example for case prefix_len == 2:
    [nonword, nonword, words[i]]
    shift list to left with rightmost bit being words[i+1]
    [nonword, words[i], words[i+1]]
    do this until no nonword elements in list
    Last element in list is the value of dict while first prefix_len elements
        are the key
    """
    i = 0
    hash_table = Hashtable(table_len)
    prefix = [NONWORD] * prefix_len + [words[i]]

    while NONWORD in prefix:
        i += 1
        prefix_str = " ".join((prefix[:prefix_len]))
        hash_table.put(prefix_str, prefix[-1])
        prefix = prefix[1:]
        prefix += [words[i]]
        
    return hash_table

def create_dict(file, prefix_len, table_len):
    """
    Creates the table for the markov chain generation
    Parameters: file -> file to create table from
                prefix_len(int) -> length of key used in dict
                table_len(int)  -> size of table
    Returns: prefix_suffix(HashTable) -> filled table
    """
    words = file.read().split()
    prefix_suffix = add_nonwords(words[:prefix_len + 1], prefix_len, table_len)

    for i in range(len(words) - prefix_len):
        prefix = " ".join((words[i:i + prefix_len]))
        suffix = words[i + prefix_len]
        prefix_suffix.put(prefix, suffix)
    return prefix_suffix

def create_chain(dict, file, prefix_len, num_words):
    """
    Creates markov chain from table according to prefix length and number
        of words requested. Will stop generation at num_words or if out of
        prefix matches.
    Paramters: dict -> table to get each word from
               file -> used to add first prefix_len words
               prefix_len(int) -> length of key used
               num_words(int) -> max words to fill chain with
    """
    words = file.readline().strip().split()
    tlist = []
    tlist += words[:prefix_len]
    prefix = " ".join(words[:prefix_len])
    while prefix in dict and len(tlist) < num_words:
        length = len(dict.get(prefix))
        if length > 1:
            word = dict.get(prefix)[random.randint(0,length - 1)]
        else:
            word = dict.get(prefix)[0]
        tlist.append(word)
        prefix = " ".join(tlist[-prefix_len:])



    return tlist
        
def print_chain(chain):
    """
    Print chain 10 words / line
    Parameters: chain(list) -> list to print 10 words per line
    """
    i = 0
    while i < len(chain):
        print(" ".join(chain[i:i + 10]))
        i += 10


def main():
    file = open(input())
    table_len = int(input())
    prefix_len= int(input())
    num_words = int(input())

    if prefix_len < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    
    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    prefix_suffix = create_dict(file, prefix_len, table_len)
    file.seek(0)
    chain = create_chain(prefix_suffix, file, prefix_len, num_words)
    print_chain(chain)
    file.close

main()