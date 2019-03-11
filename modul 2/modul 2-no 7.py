class MhsTIF(LatOOP4.Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def kataKanPy(self):
        print('Python is cool.')

# Apakah metode / state itu berasal dari class Manusia, Mahasiswa, atau MhsTIF?

# Jawab :

# Metoode atau state yang muncul berasal dari semua class baik Manusia, Mahasiswa, atau MhsTIF.
# Ini karena MhsTIF yang merupakan anak class dari Mahasiswa, dan itu membuat MhsTIF mewarisi
# semua properties dari Mahasiswa dan Manusia.
