import os
import hashlib
from blockchain import Blockchain

# Inicializa la blockchain
blockchain = Blockchain()

def hash_file(filename):
    # Función para calcular el hash SHA-256 de un archivo
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Carpeta donde están los archivos subidos por SFTP
file_directory = "/home/sftpuser/files"

for filename in os.listdir(file_directory):
    file_path = os.path.join(file_directory, filename)
    file_hash = hash_file(file_path)
    blockchain.new_file(filename, file_hash)

# Crea un nuevo bloque con los archivos y hashes actuales
last_block = blockchain.last_block()
proof = blockchain.proof_of_work(last_block['proof'])
blockchain.new_block(proof)

# Muestra la blockchain
for block in blockchain.chain:
    print(block)
