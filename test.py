import qrcode
img = qrcode.make('https://www.studio-chips.com/')
img.save('result.png')