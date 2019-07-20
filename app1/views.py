from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import  cv2
import  numpy as np


def ast1(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        img=cv2.imread(fs.path(name))
        image = cv2.resize(img, (600, 600))
        imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        value = (np.sum(imagegray))
        r = image[:, :, 0]
        g = image[:, :, 1]
        b = image[:, :, 2]
        std = (imagegray.std())
        stdr = (r.std())
        stdg = (g.std())
        stdb = (b.std())
        if (stdr < 15) or (stdg < 15) or (stdb < 15) or (std<10):
            if value < 10000000:
                text = "Camera  is covered"
            elif value > 82000000:
                text = "Camera is over lighted"
            else:
                text = "Normal Picture"
        else:
            text = "Normal Picture"
        context['result']=text
        context['path']=fs.path(name)
    return render(request, 'assignment1.html', context)



