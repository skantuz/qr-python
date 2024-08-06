import qrcode
from PIL import Image

def generate_qr_with_logo(url, logo_path, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

    logo = Image.open(logo_path)

    logo_size = min(qr_img.size) // 5
    logo = logo.resize((logo_size, logo_size))

    qr_img.paste(logo, ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2), logo)

    qr_img.save(output_path)

urls = {
    "whatsapp": "https://wa.me/elnumero",
    "github": "https://github.com/usuario",
    "linkedin": "https://linkedin.com/in/link"
}
for nombre, url in urls.items():
    logo_path = 'images/'+nombre+'.png'
    output_path = 'qrs/'+nombre+'.png'
    generate_qr_with_logo(url, logo_path, output_path)
