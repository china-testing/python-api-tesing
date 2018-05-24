import hashlib
import os
import base64


class PasswordHelper:

    def get_hash(self, plain):
        return hashlib.sha512(plain.encode('utf-8')).hexdigest()

    def get_salt(self):
        return base64.b64encode(os.urandom(20))

    def validate_password(self, plain, salt, expected):
        return self.get_hash(plain + salt) == expected
