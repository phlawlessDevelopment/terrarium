from django.shortcuts import render

from builder.models import Jar3DModel

def builder(request):
    jar = Jar3DModel.objects.filter(model_name='mason jar').first()
    jar_name = jar.file.name
    mat_name = jar.material.name
    print(jar_name)
    print(mat_name)
    context = {'jar_name':jar_name , 'mat_name':mat_name}
    return render(request, template_name='builder/builder.html', context=context)