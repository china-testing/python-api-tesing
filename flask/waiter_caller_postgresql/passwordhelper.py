import hashlib
import os
import base64

class PasswordHelper:

    def get_hash(self, plain):
        if isinstance(plain, str):
            plain = plain.encode(encoding='utf_8', errors='strict')
        return hashlib.sha512(plain).hexdigest()

    def get_salt(self):
        return base64.b64encode(os.urandom(20))

    def validate_password(self, plain, salt, expected):
        return self.get_hash(plain + salt) == expected
