from django.shortcuts import render,redirect
from django.views import View
from makanan.form import AddMakananform, EditMakananForm
from makanan.models import makanan
from django.http import HttpResponse
# Create your views here.
class LitsMakananView(View):
    templates_name = 'list_makanan.html'
    def get(self, request):
        obj = makanan.objects.all() #mengambil semua data album dari db
        print(obj)
        return render(request, self.templates_name, {
            "makanan": obj,
            "test":"Ngetes",
        })
class Meta:
    db_table = 'makanan'


class Form_Makanan(View):
    template_name = 'makanan_form.html'
    def get(self, request):
        form = AddMakananform()
        
        return render (request, self.template_name,{
            "form": form 
        })
    
    def post(self,request):
        print('data dari browser', request)
        print('data dari browser', request.POST)
        print('data dari browser', request.FILES)
        obj_new = makanan()
        form = AddMakananform(request.POST,request.FILES)
        print("isi dari form",form)
        if form.is_valid():
            pass
            print("formnya valid")
            obj_new.nama = form.cleaned_data['nama']
            obj_new.asal= form.cleaned_data['asal']
            obj_new.gambar = form.cleaned_data['gambar']
            obj_new.save()
            return redirect('./list_makanan')
        else:
            return HttpResponse(form.errors)
        return redirect('/add_makanan')   
class EditMakananView(View):
    template_name = 'edit_makanan.html'

    def get(self, request, id):
        obj = makanan.objects.get(id=id)
        data = {
            'nama':obj.nama,
            'asal':obj.asal,
            'gambar':obj.gambar,
        }
        form = EditMakananForm(initial=data)
        return render(request, self.template_name, {
            'form':form,
            'id':id #untuk mengirimkan id ke html
        })
    
    def post(self, request, id):
        obj = makanan.objects.get(id=id)
        form = EditMakananForm(request.POST)
        print(request.FILES)
        if form.is_valid():
            obj.nama = form.cleaned_data['nama']
            obj.asal = form.cleaned_data['asal']        
            if request.FILES:
                obj.gambar = request.FILES['gambar']
            obj.save()
            return redirect('/list_makanan')

class Delete(View):

    def get(self, request,pk):
        obj = makanan.objects.get(id=pk)
        obj.delete()
        return redirect ('/list_makanan') 
