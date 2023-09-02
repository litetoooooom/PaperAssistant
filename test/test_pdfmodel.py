# coding=utf-8

from paperassistant.models import PdfModel



_pdf_model = PdfModel("/data/download_model/nougat_model_small")

result = _pdf_model.parse("./test.pdf")

for k, v in result:
    print ("title: ", k)
    print ("content: ", v)