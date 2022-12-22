
from barcode import EAN13
from barcode.writer import ImageWriter
import qrcode

codigos_produtos = {
    "Excel": "551746511111",
    "Power B.I": "665789011111",
    "PowerPoint": "665887111111"}

for produto in codigos_produtos:
    codigo = codigos_produtos[produto]
    #writer = ImageWriter() usado para salvar em png, sem ele o arquivo gera um arquivo sng
    codigo_barra = EAN13(codigo, writer=ImageWriter())
    codigo_barra.save(f"codigo barra - {produto}")


links_produtos = {
    "Excel": "https://www.microsoft.com/pt-br/microsoft-365/excel",
    "Power B.I": "https://powerbi.microsoft.com/pt-br/",
    "Power Point": "https://www.microsoft.com/pt-br/microsoft-365/powerpoint",
    }


for produto in links_produtos:
    codigo = links_produtos[produto]
    imagem_qrcode = qrcode.make(codigo)
    imagem_qrcode.save(f"qrcode_python_{produto}.png")