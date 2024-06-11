# -*- encoding = utf-8 -*-

def md5_encrypt(code: str):
    import hashlib
    m = hashlib.md5()
    m.update(code.encode("utf-8"))
    return m.hexdigest()


if __name__ == '__main__':
    password = "123456"
    print(md5_encrypt(password))