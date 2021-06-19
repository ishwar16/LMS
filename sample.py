import os
import hashlib

salt = b'\xf5+\xdf\xebkX\x8f\xb7|\xed\x85\xd4'
key = hashlib.pbkdf2_hmac('sha256', 'Yok@1234 '.encode('utf-8'), salt, 100000)

storage = salt + key
print(storage[:12])
print(b'\xf5+\xdf\xebkX\x8f\xb7|\xed\x85\xd4\xe8H\xac\x12/I\xc7~\x9b9]F\xba\xec\xf5\xd5\x98\xa8\xb5 ^*<)!"\xb4\xe6hIms')
print(storage)
# class sdd:
#     password = "Yok@1234"
#     error = list()
#     def isPassRight(self, password):
#         SaltFromPassword = password[:12]
#         KeyFromPassword = password[12:]
#         newKey = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), SaltFromPassword, 100000)
#         if (KeyFromPassword == newKey):
#             return True
#         self.error.append("Given Password is wrong.")
#         return False

# s = sdd()
# d = b'\xce\xc8\xc6\x9d\xcf|H\xa0C\x07\xfd}\x9c\xf6\nvv\x84SQ\t$_\r\xcc\xdd\x04~\xb7\x88\xf67!\x90\xae}3cz\xf6~\xaf\xf5\xc6'
# print(s.isPassRight(d))
# print(str(d[:12])+"hj")