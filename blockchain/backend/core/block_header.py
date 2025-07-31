from blockchain.backend.util.util import hash256

class BlockHeader:
    """
    Represents the header of a block in the blockchain.

    The block header contains metadata required to link blocks and verify their integrity.
    This data is essential for block validation, hashing, and mining.

    Attributes:
        version (str): The version of the blockchain protocol.
        previous_block_hash (str): Hash of the previous block in the chain.
        merkle_root (str): The Merkle root hash summarizing all transactions in the block.
        time_stamp (int): Unix timestamp marking when the block was created.
        bits (str): Encoded target difficulty for the proof-of-work algorithm.
        nonce (int): A value that miners vary to find a valid block hash.
        block_hash (str): The resulting hash of the block header once a valid nonce is found.
    """

    def __init__(self, version, previous_block_hash, merkle_root, time_stamp, bits):
        self.version = version
        self.previous_block_hash = previous_block_hash
        self.merkle_root = merkle_root
        self.time_stamp = time_stamp
        self.bits = bits
        self.nonce = 0
        self.block_hash = ''

    def mine(self):
        """
        Performs a simple proof-of-work mining process.

        Continuously increments the nonce until a valid block hash is found
        that starts with four leading zeros ("0000"). Once found, the resulting
        hash is stored in `block_hash`.

        Note: This is a simplified mining algorithm used for demonstration or testing.
        """
        while self.block_hash[0:4] != '0000':
            data = (
                str(self.version) +
                self.previous_block_hash +
                self.merkle_root +
                str(self.time_stamp) +
                self.bits +
                str(self.nonce)
            )
            self.block_hash = hash256(data.encode()).hex()
            self.nonce += 1
            print(f"Mining Started {self.nonce}", end='\r')
