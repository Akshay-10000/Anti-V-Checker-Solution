import hashlib

#Global Variable
malware_hashes = list(open('vhash.txt','r').read().split('\n'))
virusInfo = list(open('vrinfo.txt','r').read().split('\n'))


#Get Hash of file
def sha256_hash(filename):
    with open(filename,'rb') as f:
        bytes = f.read()
        sha256hash = hashlib.sha256(bytes).hexdigest()
        f.close()

        print(sha256hash)
    return sha256hash

#Malware Detection By Hash
def malware_checker(pathOfFile):
    global malware_hashes
    global virusInfo

    hash_malware_check = sha256_hash(pathOfFile)
    counter = 0


    for i in malware_hashes:
        if i == hash_malware_check:
            return virusInfo[counter]
        counter += 1

    return 0


print(malware_checker('download.jpg'))

