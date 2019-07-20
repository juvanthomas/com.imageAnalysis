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


        img=cv2.imread(fs.path(name))       #image readed in colour(RGB)
        image = cv2.resize(img, (600, 600))         #converted to 600X600 pixels
        imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     #converted to grayscale
        value = (np.sum(imagegray))  # calculated the sum of values of all pixels in gray scale


        r = image[:, :, 0]      #converted to red channel
        g = image[:, :, 1]      #converted to green channel
        b = image[:, :, 2]      #converted to  blue channel
        std = (imagegray.std())     #Standard deviation of pixels values in gray scale
        stdr = (r.std())        #Standard deviation of pixels values in red channel
        stdg = (g.std())        #Standard deviation of pixels values in green channel
        stdb = (b.std())        #Standard deviation of pixels values in blue channel


        if (stdr < 15) or (stdg < 15) or (stdb < 15) or (std<10):       #If standard deviation is less then there is
            if value < 10000000:                                        # no variation in the pixels, that means
                text = "Camera  is covered"                             #either  it will be  dark or overlighted images
            elif value > 82000000:
                text = "Camera is over lighted"                         #if standard deviation is less then
            else:                                                       #sum of values of all pixels are compared to
                text = "Normal Picture"                                 #specific ranges of values
        else:
            text = "Normal Picture"                                     #the boundary values are found manually
        context['result']=text
        context['path']=fs.path(name)
    return render(request, 'assignment1.html', context)



