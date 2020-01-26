import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction= qrcode.constants.ERROR_CORRECT_M,
    box_size=15,
    border=6)

data = 'https://www.linkedin.com/in/unnati-verma-556a13172'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill= 'black', block_color= 'red')
img.save('Unnati Verma LinkedIn QRCode.png')