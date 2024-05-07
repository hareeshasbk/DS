# Program :19
# Python program to implement Hashing

HashTable =[[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(HT, keyvalue, value):
    hash_key = Hashing(keyvalue)
    HT[hash_key].append(value)
    
def Display(HT):
    for i in range(len(HT)):
        print(i, end=" ")
        for j in HT[i]:
            print("---->", end=" ")
            print(j, end="")
    
        print()
        

insert(HashTable, 42, 'Prayag') 
insert(HashTable, 24, 'mathura') 
insert(HashTable, 35, 'Vrindavan') 
insert(HashTable, 17, 'Gokul') 
insert(HashTable, 98, 'Hubli') 
insert(HashTable, 14, 'Belagavi')
insert(HashTable, 10, 'Pune') 

Display(HashTable)

