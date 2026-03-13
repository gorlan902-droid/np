from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home_view(request):
    status = request.GET.get('status')
    
    if status == 'changed': 
            message = "Текст змінено!"
    else:
            message = "просто"
            
    # Передаємо цей текст у шаблон через "контекст" (словник)
    return render(request, 'core/index.html', {'display_message': message})