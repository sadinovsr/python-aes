# Python AES with CBC

Python implementation of AES using CBC mode.

## Getting Started

### Prerequisites

Things that are needed:

- python installed
- pip installed
- Crypto library for random bytes function

```
pip install pycryptodome
```

### Usage

How to use AES:

You need to create file that you want to encrypt inside ``\documents`` folder

While inside ``\src`` folder:

```
python main.py <filename> <args>
```

where ``<filename>`` is file inside documents folder then needs to be encrypted ``<args>`` are:

- ``-e or --encrypt`` - when encrypting file (cannot be used together with -d)
- ``-d or --decrypt`` - when decrypting file (cannot be used together with -e)
- ``-g or --generate-key`` - when new key needs to be created (mandatory on first encryption call)

### Examples

Given that in ``\documents`` folder exists file ``test.doc``:

#### Encrypt

To encrypt file and generate new key:

```
python main.py test.doc -e -g
```

The above command will generate new key inside ``\src\key.key`` and will create encrypted file ``\documents\test.doc.enc`` and will delete original file ``\documents\test.doc`` and will generate initialization vector and store it in ``\src\ivs\test.doc.iv.key``

**OR**

To encrypt file with previously generated key:

```
python main.py test.doc -e
```

The above command will create encrypted file ``\documents\test.doc.enc`` and will delete original file ``\documents\test.doc`` and will generate initialization vector and store it in ``\src\ivs\test.doc.iv.key``
#### Decrypt

To decrypt the file:

```
python main.py test.doc -d
```

The above command will create decrypted file ``\documents\test.doc`` and will delete previously encrypted file ``\documents\test.doc.enc`` and will delete initialization vector from ``\src\ivs\test.doc.iv.key``
