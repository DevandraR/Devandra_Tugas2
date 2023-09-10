from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi': 'PBP_Tugas2',
        'nama': 'Devandra Reswara Arkananta',
        'kelas': 'PBP F'
    }

    return render(request, "main.html", context)