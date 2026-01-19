import hashlib, os

def generate_salt():
    return os.urandom(16)

def hash_password(password, algorithm, salt):
    pwd = password.encode()

    if algorithm == "PBKDF2":
        if salt is None:
            raise ValueError("PBKDF2 requires salt")
        return hashlib.pbkdf2_hmac(
            "sha256", pwd, salt, 150000
        ).hex()

    data = pwd if salt is None else salt + pwd

    algos = {
        "MD5": hashlib.md5,
        "SHA1": hashlib.sha1,
        "SHA256": hashlib.sha256,
        "SHA512": hashlib.sha512
    }
    return algos[algorithm](data).hexdigest()
