import sys
import time
import json

# Append the project path to allow module imports (adjust as needed)
sys.path.append('/PROYECTO ESTEGANOGRAFIA BLOCKCHAIN/blockchain-demo')

from blockchain.backend.core.block import Block
from blockchain.backend.core.block_header import BlockHeader
from blockchain.backend.util.util import hash256

# Constant representing a 64-character zero hash (used for the genesis block)
ZERO_HASH = '0' * 64

# Constant for blockchain versioning
VERSION = 1


class Blockchain:
    """
    Blockchain is a class representing the entire chain of blocks.
    It handles block creation, the genesis block, and appending new blocks to the chain.

    Attributes:
        chain (list): A list containing all blocks in the blockchain.
    """

    def __init__(self):
        """
        Initializes a new Blockchain instance with a genesis block.
        """
        self.chain = []
        self.genesis_block()

    def genesis_block(self):
        """
        Creates the first block (genesis block) in the blockchain with a predefined zero hash.
        """
        block_height = 0
        prev_block_hash = ZERO_HASH
        self.add_block(block_height, prev_block_hash)

    def add_block(self, block_height, prev_block_hash):
        """
        Adds a new block to the blockchain.

        Args:
            block_height (int): The current height of the block.
            prev_block_hash (str): The hash of the previous block in the chain.
        """
        timestamp = int(time.time())
        transaction = f"Codies Alert sent {block_height} Bitcoins to Jeo"
        merkle_root = hash256(transaction.encode()).hex()
        bits = 'ffff001f'

        # Create and mine the block header
        block_header = BlockHeader(
            VERSION,
            prev_block_hash,
            merkle_root,
            timestamp,
            bits
        )
        block_header.mine()

        # Create the block with the mined header and append to the chain
        block = Block(
            block_height,
            1,
            block_header.__dict__,  # Convert to dict for serialization
            1,
            transaction
        )
        self.chain.append(block.__dict__)

        # Pretty print the current blockchain
        print(json.dumps(self.chain, indent=4))
    
    def main(self):
        while(True):
            last_block = self.chain[::-1]
            block_height = last_block[0]['height'] + 1
            prev_block_hash = last_block[0]['block_header']['block_hash']
            self.add_block(block_height, prev_block_hash)
