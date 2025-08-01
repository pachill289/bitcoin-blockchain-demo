import sys
import time
import json

# Append the project path to allow module imports (adjust as needed)
sys.path.append('/PROYECTO ESTEGANOGRAFIA BLOCKCHAIN/blockchain-demo')

from blockchain.backend.core.block import Block
from blockchain.backend.core.block_header import BlockHeader
from blockchain.backend.util.util import hash256
from blockchain.backend.core.database.database import BlockChainDB

# Constant representing a 64-character zero hash (used for the genesis block)
ZERO_HASH = '0' * 64

# Constant for blockchain versioning
VERSION = 1


class Blockchain:
    """
    Blockchain is the main class that manages the chain of blocks.
    It provides methods to create the genesis block, add new blocks,
    store them on disk, and retrieve the latest block.

    Attributes:
        chain (list): A list containing the blockchain blocks in memory (optional).
    """

    def __init__(self):
        """
        Initializes a new instance of the Blockchain class
        and creates the genesis block.
        """
        self.chain = []
        self.genesis_block()

    def write_on_disk(self, block):
        """
        Writes the given block(s) to the persistent storage using BlockChainDB.

        Args:
            block (list): A list of block dictionaries to be written to disk.
        """
        blockchain_db = BlockChainDB()
        blockchain_db.write(block)

    def fetch_last_block(self):
        """
        Retrieves the latest block from the blockchain storage.

        Returns:
            dict: The most recent block stored in the blockchain.
        """
        blockchain_db = BlockChainDB()
        return blockchain_db.last_block()

    def genesis_block(self):
        """
        Creates and stores the first block (genesis block) in the blockchain,
        using a predefined zero hash as the previous hash.
        """
        block_height = 0
        prev_block_hash = ZERO_HASH
        self.add_block(block_height, prev_block_hash)

    def add_block(self, block_height, prev_block_hash):
        """
        Adds a new block to the blockchain based on the previous block's hash.

        Args:
            block_height (int): The height of the new block.
            prev_block_hash (str): The hash of the previous block.
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

        # Create the new block
        block = Block(
            block_height,
            1,
            block_header.__dict__,  # Convert header to dictionary
            1,
            transaction
        )

        # Write the block to disk
        self.write_on_disk([block.__dict__])

        # Optional: print block data (for debugging or testing)
        # print(json.dumps(self.chain, indent=4))

    def main(self):
        """
        Starts the blockchain mining loop.
        Continuously fetches the last block and appends new blocks to the chain.
        """
        while True:
            last_block = self.fetch_last_block()
            block_height = last_block['height'] + 1
            prev_block_hash = last_block['block_header']['block_hash']
            self.add_block(block_height, prev_block_hash)
