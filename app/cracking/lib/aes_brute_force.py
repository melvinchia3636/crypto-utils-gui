import time
from PyQt5.QtCore import QThread, pyqtSignal
from Crypto.Cipher import AES


class AesBruteForceWorker(QThread):
    progress = pyqtSignal(object, object, float)
    found = pyqtSignal(bytes, str)
    not_found = pyqtSignal()

    def __init__(self, nonce, tag, ciphertext, known_prefix, key_start, key_end):
        super().__init__()
        self._nonce = nonce
        self._tag = tag
        self._ct = ciphertext
        self._known = known_prefix
        self._start = key_start
        self._end = key_end
        self._cancelled = False

    def run(self):
        total = self._end - self._start
        start_time = time.time()
        report_step = max(1, min(total // 200, 10000))

        for i, key_int in enumerate(range(self._start, self._end)):
            if self._cancelled:
                return

            key = key_int.to_bytes(16, "big")

            try:
                cipher = AES.new(key, AES.MODE_GCM, nonce=self._nonce)
                pt = cipher.decrypt_and_verify(self._ct, self._tag)
                text = pt.decode("utf-8", errors="ignore")

                if self._known in text:
                    self.found.emit(key, text)
                    return
            except Exception:
                pass

            if i > 0 and i % report_step == 0:
                elapsed = time.time() - start_time
                self.progress.emit(i, total, elapsed)

        self.not_found.emit()

    def cancel(self):
        self._cancelled = True
