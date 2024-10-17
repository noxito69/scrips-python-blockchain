import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_files = []

        # Crea el bloque génesis
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        # Crea un nuevo bloque en la blockchain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'files': self.current_files,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Resetea la lista de archivos actuales
        self.current_files = []
        self.chain.append(block)
        return block

    def new_file(self, file_name, file_hash):
        # Añade un nuevo archivo a la lista de archivos actuales
        self.current_files.append({
            'file_name': file_name,
            'file_hash': file_hash,
        })

    @staticmethod
    def hash(block):
        # Hashea un bloque
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def last_block(self):
        # Retorna el último bloque en la cadena
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        # Simple algoritmo de prueba de trabajo
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        # Valida la prueba
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
