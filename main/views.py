from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406495773',
        'name': 'Abigail Namaratonggi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
