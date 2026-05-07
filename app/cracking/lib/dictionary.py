import time
from PyQt5.QtCore import QThread, pyqtSignal


def _count_lines(path):
    count = 0
    with open(path, encoding="utf-8", errors="ignore") as f:
        for _ in f:
            count += 1
    return count


class DesDictionaryWorker(QThread):
    progress = pyqtSignal(object, object, float)
    found = pyqtSignal(bytes, str)
    not_found = pyqtSignal()

    def __init__(self, iv, ciphertext, known_prefix, wordlist_path):
        super().__init__()
        self._iv = iv
        self._ct = ciphertext
        self._known = known_prefix
        self._path = wordlist_path
        self._cancelled = False

    def run(self):
        from Crypto.Cipher import DES
        from Crypto.Util.Padding import unpad
        from Crypto.Hash import SHA256
        from Crypto.Protocol.KDF import PBKDF2

        total = _count_lines(self._path)
        start_time = time.time()
        count = 0

        with open(self._path, encoding="utf-8", errors="ignore") as f:
            for line in f:
                if self._cancelled:
                    return

                passphrase = line.strip()
                if not passphrase:
                    count += 1
                    continue

                key = PBKDF2(
                    passphrase,
                    b"cryptofun",
                    dkLen=8,
                    count=100000,
                    hmac_hash_module=SHA256,
                )

                try:
                    cipher = DES.new(key, DES.MODE_CBC, iv=self._iv)
                    pt = unpad(cipher.decrypt(self._ct), 8)
                    text = pt.decode("utf-8", errors="ignore")

                    if self._known in text:
                        self.found.emit(key, text)
                        return
                except Exception:
                    pass

                count += 1
                if count % 100 == 0:
                    elapsed = time.time() - start_time
                    self.progress.emit(count, total, elapsed)

        self.not_found.emit()

    def cancel(self):
        self._cancelled = True


class AesDictionaryWorker(QThread):
    progress = pyqtSignal(object, object, float)
    found = pyqtSignal(bytes, str)
    not_found = pyqtSignal()

    def __init__(self, nonce, tag, ciphertext, known_prefix, wordlist_path):
        super().__init__()
        self._nonce = nonce
        self._tag = tag
        self._ct = ciphertext
        self._known = known_prefix
        self._path = wordlist_path
        self._cancelled = False

    def run(self):
        from Crypto.Cipher import AES
        from Crypto.Hash import SHA256
        from Crypto.Protocol.KDF import PBKDF2

        total = _count_lines(self._path)
        start_time = time.time()
        count = 0

        with open(self._path, encoding="utf-8", errors="ignore") as f:
            for line in f:
                if self._cancelled:
                    return

                passphrase = line.strip()
                if not passphrase:
                    count += 1
                    continue

                key = PBKDF2(
                    passphrase,
                    b"cryptofun",
                    dkLen=16,
                    count=100000,
                    hmac_hash_module=SHA256,
                )

                try:
                    cipher = AES.new(key, AES.MODE_GCM, nonce=self._nonce)
                    pt = cipher.decrypt_and_verify(self._ct, self._tag)
                    text = pt.decode("utf-8", errors="ignore")

                    if self._known in text:
                        self.found.emit(key, text)
                        return
                except Exception:
                    pass

                count += 1
                if count % 100 == 0:
                    elapsed = time.time() - start_time
                    self.progress.emit(count, total, elapsed)

        self.not_found.emit()

    def cancel(self):
        self._cancelled = True
