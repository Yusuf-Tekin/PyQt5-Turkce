from PyQt5 import QtWidgets,QtGui
import sys

class myMain:
    def PencereYarat(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        """Ekranda Beliren ve İşletim Sistemine Uygun Boş Pencere Yaratır"""

    def PencereGoster(self):
        self.window.show()
        sys.exit(self.app.exec_())
        """Oluşturulan Pencere'yi Ekranda Göstermeye Yarar"""

    def PencereGenislik(self,genislik):
        self.window.setFixedWidth(genislik)
        """Pencere'ye Sabit Genişlik Verir"""

    def PencereYukseklık(self,yukseklik):
        self.window.setFixedHeight(yukseklik)
        """Pencere'ye Sabit Yükseklik Verir"""

    def PencereBaslik(self,baslik):
        self.window.setWindowTitle(baslik)
        """Pencere Başlığı Belirtir"""
    def PencereIkon(self,yol):
        self.window.setWindowIcon(QtGui.QIcon(yol))
        """Pencere'nin İkonu Değiştirir"""

    def PencereArkaPlanRengi(self,renk):
        self.window.setStyleSheet('background-color: %s' %renk)
        """Pencere Arkaplan Rengi Değiştirir"""
    def PencereBoyutu(self,genislik,yukseklik):
        self.window.resize(genislik,yukseklik)
        """Pencere'nin Boyutunu değişken biçimde ayarlar"""
    def PencereKonumu(self,x,y):
        self.window.move(x,y)
        """Pencere'nin Ekranda görüneceği konumu ayarlar"""
    def PencereMaksimumGenislik(self,genislik):
        self.window.setMaximumWidth(genislik)
        """Pencere'ye verilebilecek max genişlik özelliğini verir"""
    def PencereMaksimumYukseklik(self, yukseklik):
        self.window.setMaximumWidth(yukseklik)
        """Pencere'ye verilebilecek max yükseklik özelliğini verir"""
    def PencereMaksimumBoyut(self,maksgenislik,maksyukseklik):
        self.window.setMaximumSize(maksgenislik,maksyukseklik)
        """Pencere'Nin Maksimum Genişlik Ve Yükseklik Oranını verir
            Yukarıdaki 2 fonksiyonun birleştirilmiş halidir
        """
    def PencereTamEkran(self):
        self.window.showFullScreen()
        """Pencere'yi Oyun Ekranı gibi tam ekran gösterir"""
    def PencereTamBoyut(self):
        self.window.showMaximized()
        """Pencereyi üst durum çubuğu kalacak şekilde tam boyutlu gösterir"""
    def PencereSaydamlık(self,saydamlik):
        """Pencere Saydamlığını Belirtir. Saydamlık Değer 0 ile 1 arasında olmalıdır."""
        if(saydamlik > 1 or saydamlik < 0):
            self.window.setWindowOpacity(1)
            """Pencere Saydamlığı 1'den büyük veya 0'dan kğçük değer alırsa otomatik değer 1'e atanır"""
        else:
            self.window.setWindowOpacity(saydamlik)
            """Pencere Saydamlık Değeri 0 ve 1 arasında değer verilmişse kullanıcını değeri atanır"""



window = myMain()