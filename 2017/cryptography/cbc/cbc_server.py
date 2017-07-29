import SocketServer
import os
from Crypto.Cipher import AES
import rahasia

HOST, PORT = "0.0.0.0", 9876

banner = "Kamu bisa coba: masuk, keluar, bendera\n"

class MyTCPHandler(SocketServer.BaseRequestHandler):

    def enkrip(self, data):
        length = 16 - (len(data) % 16)
        data += chr(length) * length
        cipher = AES.new(self.kunci, AES.MODE_CBC, self.IV)
        ciphertext = cipher.encrypt(data)
        return self.IV + ciphertext

    def denkrip(self, data):
        IV   = data[:16]
        data = data[16:]
        cipher = AES.new(self.kunci, AES.MODE_CBC, IV)
        plaintext = cipher.decrypt(data)
        plaintext = plaintext[:-ord(plaintext[-1])]
        return plaintext

    def cmd_masuk(self):
        if self.sudah_masuk:
            self.request.send("    kamu sudah masuk!\n")
        else:
            self.request.send("    username: ")
            username = self.request.recv(1024).strip()
            if len(username) < 8:
                self.request.send("    kurang panjang!\n")
            elif not username.isalnum():
                self.request.send("    tidak valid!\n")
            else:
                sign = username + "|" + "user"
                enc  = self.enkrip(sign)
                self.request.send("    signature kamu: " + enc.encode("hex") + "\n")
                self.sudah_masuk = True

    def cmd_bendera(self):
        if not self.sudah_masuk:
            self.request.send("    kamu belum masuk!\n")
        else:
            self.request.send("    signature: ")
            enc = self.request.recv(1024).strip()
            sign = self.denkrip(enc.decode("hex"))
            role = sign.split('|')[1]
            if role == "admin":
                self.request.send("    berhasil: " + rahasia.bendera + "\n")
                self.request.close()
            else:
                self.request.send("    gagal: kamu bukan admin tapi " + role + "\n")

    def shell(self):
        while True:
            self.request.send(">>> ")
            cmd = self.request.recv(1024).strip()
            if cmd == "" or cmd == "keluar":
                break
            elif cmd == "masuk":
                self.cmd_masuk()
            elif cmd == "bendera":
                self.cmd_bendera()

    def handle(self):
        self.IV  = os.urandom(16)
        self.kunci = os.urandom(32)
        self.sudah_masuk = False
        self.request.sendall(banner)
        self.shell()
        self.request.close()

if __name__ == "__main__":
    SocketServer.ThreadingTCPServer.allow_reuse_address = True
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()