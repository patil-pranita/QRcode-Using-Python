import qrcode
from PIL import Image
qrcode = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=10,)

qrcode.add_data("https://github.com/patil-pranita")
qrcode.make(fit=True)
img= qrcode.make_image(fill_color="purple",back_color="white")
img.save("Pranita_GitHubPage.png")