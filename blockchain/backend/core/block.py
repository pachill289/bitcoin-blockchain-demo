class Block:
    """
    Represents a block in the blockchain.

    A block is a fundamental data structure used to store a group of transactions.
    Each block includes metadata (block header) and a list of transactions, and is 
    linked to previous blocks to form a secure and immutable chain.

    Attributes:
        height (int): The position of the block in the blockchain (block number).
        block_size (int): The size of the block in bytes.
        block_header (dict): The header containing essential metadata (e.g., previous hash, timestamp, merkle root).
        tx_count (int): The number of transactions included in the block.
        txs (list): A list of transaction data contained in the block.
    """
    def __init__(self, height, block_size, block_header, tx_count, txs):
        self.height = height
        self.block_size = block_size
        self.block_header = block_header
        self.tx_count = tx_count
        self.txs = txs