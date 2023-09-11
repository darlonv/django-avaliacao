import qrcode
import json

# TRABALHOS_FILE = "scripts/trabalhos.json"
TRABALHOS_FILE = "trabalhos.json"
LINK_PREFIX = "http://127.0.0.1/avaliar/?tid="


def gen_save_qrcode(url, img_filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(img_filename)


with open(TRABALHOS_FILE, "r") as file:
    trabalhos = json.load(file)

    for tid in trabalhos:
        link = f"{LINK_PREFIX}{tid}"
        img_filename = f"qr_images/{tid}.png"
        gen_save_qrcode(link, img_filename)
