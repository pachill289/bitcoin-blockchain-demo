# 🧱 Blockchain Demo Project

This is a demo project simulating a basic blockchain structure developed in Python. It includes essential components such as block creation, block headers, transaction hashing using SHA-256, and proof-of-work mining. The project is modular, with a backend for blockchain logic and a frontend interface to be added later.

## 📂 Project Structure

```
BLOCKCHAIN-DEMO/
├── .venv/                         # Python virtual environment
├── blockchain/
│   ├── backend/
│   │   ├── core/
│   │   │   ├── block.py          # Block class
│   │   │   ├── block_header.py   # BlockHeader class
│   │   │   └── blockchain.py     # Blockchain logic
│   │   └── util/
│   │       └── util.py           # Utility functions (e.g. hash256)
│   └── frontend/                 # (To be developed)
├── main.py                       # Entry point for testing
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## 🚀 Features

- Custom `Block` and `BlockHeader` classes.
- Double SHA-256 hashing (similar to Bitcoin).
- Basic Proof-of-Work mining mechanism.
- Genesis block creation and chain appending.
- Terminal output of the blockchain in JSON format.

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/blockchain-demo.git
cd blockchain-demo
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

On Unix or MacOS:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Running the Project

To run the project, ensure you're in the root directory and execute:

```bash
python main.py
```

This script will initialize a blockchain, create a genesis block, and add a new block using a mined header.

> 🔍 **Tip:** For debugging and inspecting block generation, place a breakpoint inside `blockchain.py` at the block creation section. This is helpful to verify how the blocks are being generated and whether they are linked correctly.

## 🛠 VS Code Configuration

To ensure VS Code uses the correct virtual environment, add the following to your `.vscode/settings.json` file:

```json
{
  "python.pythonPath": "D:\\PROYECTO ESTEGANOGRAFIA BLOCKCHAIN\\blockchain-demo\\.venv\\Scripts\\python.exe"
}
```

This allows VS Code to automatically recognize and use your Python virtual environment for linting, debugging, and execution.

## 📄 License

This project is licensed under the **Apache License 2.0**. See the LICENSE file for full license information.

## 💬 Contribution & Feedback

This is a learning and experimentation project. Contributions are welcome for improving blockchain components, adding unit tests, or building the frontend interface.

Feel free to fork the repository and open a pull request!

## 📧 Contact

For suggestions or inquiries, feel free to reach out via GitHub Issues or email.
