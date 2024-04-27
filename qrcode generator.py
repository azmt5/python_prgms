import qrcode
import image
qr=qrcode.QRCode(
    version=15, # means the version of the qr code higher the number bigger than code image and compilcated img.
    box_size=10, # size of box where qr code will be displayed
    border=5,# it is white part of the image
)
data="https://www.youtube.com/channel/UCfFI-WZZwTzNkmaChKCq0jg"
# if you redirct 

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")


