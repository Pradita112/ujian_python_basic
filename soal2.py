class Kelas:
    def __init__(self,jumlah_siswa:int, kapasitas:int):
        self.js = jumlah_siswa
        self.kp = kapasitas
    
    def info(self):
        print("ini adalah kelas")
        
class Fisika(Kelas):
    def info(self):
        print("ini adalah kelas fisika")

k = Fisika(40,2)
k.info()