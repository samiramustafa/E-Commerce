# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Product
# from .forms import ProductForm

# @login_required
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.added_by = request.user  ###### تسجيل المستخدم الحالي تلقائيًا
#             product.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form': form})


