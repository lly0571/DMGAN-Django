import imp
from cv2 import split
from django.shortcuts import render,get_object_or_404

from ImageGenerate.forms import TextUploadForm

from .DMGAN.code.main import *


algo,split_dir,ds=LoadModel()

def index(request):
    description=''
    path = './ImageGenerate/DMGAN/data/birds/example_captions.txt'
    if request.method == 'POST':
        form = TextUploadForm(request.POST, request.FILES)
        
        # form2=request.FILES.get('mask')

        if form.is_valid() :
            # passing the image as base64 string to avoid storing it to DB or filesystem？
            #转base64可以不进数据库？

            # image = form.cleaned_data['image']
            # image_bytes = image.file.read()
            # encoded_img = base64.b64encode(image_bytes).decode('ascii')
            # image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)
            # print("Image Uploaded").
            description=form.cleaned_data['description']
            with open(path,'w')as f:
                f.write(description)
            
            # print(image_uri)
#负责mask数据的表单
            # cv2.imwrite("img.png", encoded_img)

            # mask_file = form.cleaned_data['mask']
            # mask_bytes = mask_file.file.read()
            # encoded_mask = base64.b64encode(mask_bytes).decode('ascii')
            # mask_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_mask)
            # print("Mask Uploaded")

            # get predicted label.
            try:
                os.remove('./ImageGenerate/static/1.png')
            except:
                pass
            try:
                Generate(algo,split_dir,ds)

            except RuntimeError as re:
                print("Generation Error",re)
                # predicted_label = "Prediction Error"

    else:
        form = TextUploadForm()

    context = {
        'form': form,
        'img_gen': description+'.png',
    }
    return render(request, 'ImageGenerate/index.html', context)