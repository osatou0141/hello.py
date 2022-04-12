import segno
qrcode = segno.make('hello')
qrcode.save('qrcode.png')
qrcode.show()
