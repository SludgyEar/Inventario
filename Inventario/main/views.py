from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main_view(request):
    return render(request, 'mainTemplate/mainTemplate.html')

# Se pueden agregar más vistas de la siguiente forma:
# def saved_recipes(request):
#     return render(request, 'saved_recipes_template/saved_recipes.html')

