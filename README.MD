# Python AES with CBC

Python implementation of AES using CBC mode.

## Getting Started

### Prerequisites

Things that are needed:

- python installed
- pip installed
- need to create folder named 'ivs' inside src folder
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

Given that in ``\documents`` folder exists file ``test.txt``:

#### Encrypt

To encrypt file and generate new key:

```
python main.py test.txt -e -g
```

The above command will generate new key inside ``\src\key.key`` and will create encrypted file ``\documents\test.txt.enc`` and will delete original file ``\documents\test.txt`` and will generate initialization vector and store it in ``\src\ivs\test.txt.iv.key``

**OR**

To encrypt file with previously generated key:

```
python main.py test.txt -e
```

The above command will create encrypted file ``\documents\test.txt.enc`` and will delete original file ``\documents\test.txt`` and will generate initialization vector and store it in ``\src\ivs\test.txt.iv.key``
#### Decrypt

To decrypt the file:

```
python main.py test.txt -d
```

The above command will create decrypted file ``\documents\test.txt`` and will delete previously encrypted file ``\documents\test.txt.enc`` and will delete initialization vector from ``\src\ivs\test.txt.iv.key``
