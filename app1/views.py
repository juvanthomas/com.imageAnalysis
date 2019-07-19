from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import  cv2
import  numpy as np


def ast1(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        img=cv2.imread(fs.path(name),0)
        image = cv2.resize(img, (600, 600))
        value = (np.sum(image))
        if value < 10000000:
            text="Camera is covered"
        elif value > 82800000:
            text="Camera is over lighted"
        else:
            text="Normal picture"
        print(text,value)
        context['result']=text
        context['path']=fs.path(name)
    return render(request, 'assignment1.html', context)



