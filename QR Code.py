import qrcode

qr = qrcode.make('https://www.linkedin.com/in/unnati-verma-556a13172')
qr.save('myQR.png')