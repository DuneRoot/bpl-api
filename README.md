# BPL API

> A simple Python API for the Blockpool blockchain

This is a easy-to-use Python API for interacting with a Blockpool blockchain. This API provides a Python wrapper for the majority of the API endpoints for [BPL-Node](https://github.com/blockpool-io/BPL-node)

## Features

### Accounts Endpoint
- [x] Retrieve an account
- [x] Retrieve the balance of an account
- [x] Retrieve the public key of an account
- [x] Retrieve the delegate registration fee
- [x] Retrieve the voted delegate of an account

### Blocks Endpoint
- [x] Retrieve for a block
- [x] List all blocks
- [x] Retrieve the epoch of the blockchain
- [x] Retrieve the height of the blockchain
- [x] Retrieve the nethash of the blockchain
- [x] Retrieve a fee
- [x] List all fees of the blockchain
- [x] Retrieve the milestone of the blockchain
- [x] Retrieve the reward of the blockchain
- [x] Retrieve the supply of the blockchain
- [x] Retrieve the status of the blockchain

### Delegates Endpoint
- [x] Retrieve a delegate
- [x] Retrieve the total count of delegates
- [x] Retrieve the delegate registration fee
- [x] Retrieve the total forged of a delegate
- [x] List all voters of a delegate
- [x] List all delegates
- [x] Search all delegates
- [x] List the next forgers
- [x] Retrieve the forging status of a delegate

### Loader Endpoint
- [x] Retrieve the status of the connected node
- [x] Retrieve the synchronisation status of the connected node
- [x] Retrieve the configuration of the connected node

### Multisignature Endpoint
- [x] Retrieve the pending multisignature transactions of an account
- [ ] Retrieve a multisignature account

### Peers Endpoint
- [x] Retrieve a peer
- [x] List all peers
- [x] Retrieve the core version

### Signatures Endpoint
- [x] Retrieve the signature registration fee

### Transaction Endpoint
- [x] Retrieve a transaction
- [x] List all transactions
- [x] Retrieve an unconfirmed transaction
- [x] List all unconfirmed transactions
- [x] Send a transaction

### Endpoint Entity
- [x] GET
- [x] POST
- [x] PUT
- [x] DELETE

## Installation

```sh
python -m pip install bpl-api
```

## Usage

There are 8 API endpoints in bpl-api:

- ``accounts``
- ``blocks``
- ``delegates``
- ``loader``
- ``multisignatures``
- ``peers``
- ``signatures``
- ``transactions``

Each endpoint can be accessed using the `Client` interface, for example:
```python
from bpl_api import Client

accounts_endpoint = Client("s01.mc.blockpool.io:9030").api("accounts")
```

See the documented code for how each endpoint may be used.

## Security or Errors


If you discover a security vulnerability or error within this package, please email [me](mailto:alistair@duneroot.co.uk) or message me on the [BPL discord](https://discordapp.com/invite/67HxSKq).

## Credits

- [Alistair O'Brien](https://github.com/johnyob)
