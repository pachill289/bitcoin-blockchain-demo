import os
import json

class BaseDB:
    """
    BaseDB handles basic read and write operations for storing blockchain data.
    
    Attributes:
        file_name (str): The name of the file where the blockchain will be stored.
        base_path (str): The base directory to store the blockchain file.
        file_path (str): The complete path to the blockchain file.
    """
    def __init__(self):
        self.file_name = "blockchain"
        self.base_path = 'data'
        self.file_path = '/'.join((self.base_path, self.file_name))
    
    def read(self):
        """
        Reads and returns blockchain data from the file.
        
        Returns:
            list or bool: Returns the parsed blockchain data as a list if available, otherwise False.
        """
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} not available")
            return False
        with open(self.file_path, 'r') as file:
            raw = file.readline()
        
        if len(raw) > 0:
            data = json.loads(raw)
        else:
            data = []
        return data

    def write(self, item):
        """
        Writes a list of blocks to the blockchain file.
        
        If the blockchain already exists, appends the new blocks.
        If not, it writes the new data as the genesis block.
        
        Args:
            item (list): A list of blocks (as dictionaries) to be written.
        """
        data = self.read()
        if data:
            data = data + item
        else:
            data = item
        with open(self.file_path, "w+") as file:
            file.write(json.dumps(data))

class BlockChainDB(BaseDB):
    """
    BlockChainDB inherits from BaseDB and provides specific methods for blockchain operations.
    It is the main database class for storing and retrieving blockchain data.
    """
    def __init__(self):
        super().__init__()

    def last_block(self):
        """
        Retrieves the most recent block from the blockchain.
        
        Returns:
            dict or None: Returns the last block as a dictionary if data exists, otherwise None.
        """
        data = self.read()
        if data:
            return data[-1]
