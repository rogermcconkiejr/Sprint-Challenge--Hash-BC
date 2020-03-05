import hashlib
import requests

import sys
import json

from uuid import uuid4

from timeit import default_timer as timer

import time as time

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()    
    print("Searching for next proof")
    proof = 0
    # while True:
    #     proof += random.randint(1, 1024)
    #     r = requests.get(url=node + "/last_proof", headers={'Authorization': 'Token e248d14d709d55c96b7607e45d143a34ae65d823'})
    #     data = r.json()
    #     print(data)
    #     lp = data['proof']
    #     dif = data["difficulty"]
    #     if valid_proof(lp, proof, dif):
    #         return proof 
    #     time.sleep(1)
    while valid_proof(last_proof, proof) is False:
            proof += random.randint(1, 1024)
    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """
    difficultyLevel =  data["difficulty"]
    lastProof = data["proof"]

    # plug_in = f'{last_hash}'.encode() ## Last hash has to be filled in with response
    # check_last = hashlib.sha256(plug_in).hexdigest()
    guess = f'{last_hash}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    return guess_hash[:difficultyLevel] == '0' * difficultyLevel 


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-treasure-hunt.herokuapp.com/api/bc"

    coins_mined = 0


    while True:
        # Get the last proof from the server

        r = requests.get(url=node + "/last_proof", headers={'Authorization': 'Token e248d14d709d55c96b7607e45d143a34ae65d823'})
        data = r.json()
        print(data)
        print(data['proof'])
        print(data["difficulty"])
        time.sleep(1)
        lp = data['proof']
        new_proof = proof_of_work(data.get('proof'))
        post_data = {"proof": new_proof}

        r = requests.post(url=node + "/mine", json=post_data, headers={'Authorization': 'Token e248d14d709d55c96b7607e45d143a34ae65d823'})
        data = r.json()
        print(data)
        time.sleep(data['cooldown'])
