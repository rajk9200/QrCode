from django.shortcuts import render
#from qr_code.qrcode.utils import QRCodeOptions
from django.contrib import messages
from django.http import HttpResponse
import pyqrcode
import qrcode
from django.contrib import auth

# Create your views here.
def QRcode(request):
    data = request.POST.get('data')  # gets input from user to encode into qrcode
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10,
                       border=4, )  # initialize settings for Output Qrcode
    qr.add_data(data)  # adds the data to the qr cursor

    qr.make(fit=True)
    img = qr.make_image()

    file_name = request.POST.get('file_name')
    file_extension = request.POST.get('file_extension')

    try:
        file_name =file_name +'.'+ file_extension
        image_file = open(file_name, 'wb+')
        image_file=img.save(image_file,file_extension.upper())  # write qrcode encoded data to the image file.
        image_file=img.show()
        image_file.close()
    except:
        message="Added successfully"

    context = {

        "data": data,
        "file_name": file_name,
        "file_extension": file_extension,
    }
    print("success")
    return render(request, "showqr.html", context)
