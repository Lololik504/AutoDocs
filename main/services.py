import tempfile
from django.http import HttpResponse, request
from django.template import loader, RequestContext

from AutoDocs import settings
import zipfile
from .models import Singers
import os
import docx


def handling(f):
    with open('main/docs/text.doc', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return main_function()


def main_function():
    zip = zipfile.ZipFile(settings.DOCUMENT_ROOT + 'archive.zip', 'w')
    singers = Singers.objects.all()
    print(singers)
    for singer in singers:
        doc = docx.Document(os.path.join(settings.DOCUMENT_ROOT, "text.doc"))
        print(singer)
        for paragraph in doc.paragraphs:
            for word in paragraph.runs:
                if word.text == " __имя__":
                    word.clear()
                    word.add_text(' ' + singer.firstname + ' ' + singer.lastname)
        file_name = singer.firstname + ' ' + singer.lastname + '.doc'
        file_abs_name = settings.DOCUMENT_ROOT + file_name
        doc.save(file_abs_name)
        zip.write(file_abs_name, file_name, compress_type=zipfile.ZIP_DEFLATED)
        os.remove(file_abs_name)
    os.remove(os.path.join(settings.DOCUMENT_ROOT, "text.doc"))
    zip.close()
    print(zip.filename)
    return zip.filename
