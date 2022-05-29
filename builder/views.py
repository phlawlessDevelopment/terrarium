from django.shortcuts import render

from builder.models import Jar3DModel

def builder(request):
    jar_url = Jar3DModel.objects.first().file.url
    context = {'jar_url':jar_url}
    print(jar_url)
    return render(request, template_name='builder/builder.html', context=context)