from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages


from django.views.generic import View

from .forms import (CategoryCreateForm,
                    ProductCreateForm,
                    ShopCreateForm,
                    ShopUpdateForm,
                    ShopProductUpdateForm,
                    ShopProductCreateForm,
                    ProductSelectPriceForm,
                    ProductSearchForm)
from .models import *


def main_menu_page(request):
    return render(request, 'products/main_page.html')

def shop_list(request):
    shops=Shop.objects.all()
    return render(request, 'products/shop_list.html', context={'shops':shops})

def product_list(request):
    products=Product.objects.all()
    return render(request, 'products/product_list.html', context={'products':products})

def product_list_sort_price(request):
    products=Product.objects.order_by('price')
    return render(request, 'products/product_list.html', context={'products':products})

def product_list_active(request):
    products=Product.objects.filter(active=True)
    return render(request, 'products/product_list.html', context={'products':products})


def category_list(request):
    categories=Category.objects.all()
    return render(request, 'products/category_list.html', context={'categories':categories})

class ShopDetailView(View):

    def get(self,request, pk):
        shop=Shop.objects.get(id=pk)
        return render(request, 'products/shop_detail.html',context={'shop':shop})

    
    
class ProductDetailView(View):

    def get(self,request, pk):
        prod=Product.objects.get(id=pk)
        main_image=prod.productimage_set.all()[0]
        other_images=prod.productimage_set.all()[1:]
        return render(request, 'products/product_detail.html',context={'prod':prod, 'main_image':main_image,'other_images':other_images})

class CategoryDetailView(View):

    def get(self,request, pk):
        category=Category.objects.get(id=pk)
        prod_list=Product.objects.filter(category=category.id)
        return render(request, 'products/category_detail.html',context={'category':category, 'prod_list':prod_list})

class CategoryCreateView(View):

    def get(self,request):
        
        form=CategoryCreateForm()
        
        return render(request, 'products/category_create.html',context={'form':form})
    
    def post(self,request):
        bound_form=CategoryCreateForm(request.POST)
        if bound_form.is_valid():
            new_cat=bound_form.save()
            return redirect(new_cat)
        else:
            return render(request, 'products/category_create.html',context={'form':bound_form})



class ProductCreateView(View):

    def get(self,request):
        
        form=ProductCreateForm()
        
        return render(request, 'products/product_create.html',context={'form':form})
    
    def post(self,request):
        bound_form=ProductCreateForm(request.POST)
        if bound_form.is_valid():
            new_prod=bound_form.save()
            return redirect(new_prod)
        else:
            return render(request, 'products/product_create.html',context={'form':bound_form})

class ProductUpdateView(View):

    def get(self,request,pk):
        prod=Product.objects.get(id=pk)
        form=ProductCreateForm(instance=prod)
    
        context={'form':form
                }
        return render(request, 'products/product_update.html',context=context)
    
    def post(self,request,pk):
        prod=Product.objects.get(id=pk)
        bound_form=ProductCreateForm(request.POST,instance=prod)
       
        if bound_form.is_valid():
            new_prod=bound_form.save()
            return redirect(new_prod)
        else:
            return render(request, 'products/product_update.html',context=context)

class ProductSelectPriceView(View):

    def get(self,request):

        if request.GET:
        
            form=ProductSelectPriceForm(initial={'min_price':0.0, 'max_price':0.0})
            products=Product.objects.filter(price__range=(request.GET['min_price'],request.GET['max_price']))
            if len(products)>0:
                messages.success(request, f'Список товаров')
                return render(request, 'products/product_select_price.html',context={'form':form,'prod':products,})
            else:
                messages.warning(request, f'В таком ценовом диапазоне товаров нет')
                return render(request, 'products/product_select_price.html',context={'form':form})
                
        else:
            form=ProductSelectPriceForm(initial={'min_price':0.0, 'max_price':0.0})
    
            return render(request, 'products/product_select_price.html',context={'form':form})
            
        
class ProductSearchView(View):

    def get(self,request):

        if request.GET:
        
            form=ProductSearchForm(initial={'title':''})
            products=Product.objects.filter(title__icontains=request.GET['title'])
        
          
            return render(request, 'products/product_search.html',context={'form':form,'prod':products})
          
                
        else:
            form=ProductSearchForm(initial={'title':''})
    
            return render(request, 'products/product_search.html',context={'form':form})
            
        

class ShopCreateView(View):

    def get(self,request):
        
        form=ShopCreateForm()
        form_p=ShopProductCreateForm()
        return render(request, 'products/shop_create.html',context={'form':form,
                                                                    'products':form_p['products'].as_widget(forms.CheckboxSelectMultiple(choices=[(p.title,p.title) for p in Product.objects.all()]))})
    
    def post(self,request):
        bound_form=ShopCreateForm(request.POST,request.FILES)
        form_p=ShopProductCreateForm(request.POST)
        if bound_form.is_valid():
            new_shop=bound_form.save()
            new_shop.products.set(Product.objects.filter(title__in=form_p['products'].value()))
            new_shop.save()
            return render(request, 'products/shop_create.html',context={'form':bound_form,'s':(request.POST, new_shop)})#redirect(new_shop)
        else:
            return render(request, 'products/shop_create.html',context={'form':bound_form,
                                                                        'products':form_p['products'].as_widget(forms.CheckboxSelectMultiple(choices=[(p.title,p.title) for p in Product.objects.all()]))})
class ShopUpdateView(View):

    def get(self,request,pk):
        shop=Shop.objects.get(id=pk)
        form=ShopUpdateForm(instance=shop)
        form_p=ShopProductUpdateForm()
        query=[(p.title,p.title) for p in shop.products.all()]
        query_add=[(p.title,p.title) for p in Product.objects.all() if p not in shop.products.all()]
        context={'form':form,
                 'shop':shop,
                 'products':form_p['products'].as_widget(forms.CheckboxSelectMultiple(choices=query)),
                 'products_add':form_p['products_add'].as_widget(forms.CheckboxSelectMultiple(choices=query_add))}
        return render(request, 'products/shop_update.html',context=context)
    
    def post(self,request,pk):
        new_prods=[]
        shop=Shop.objects.get(id=pk)
        bound_form=ShopUpdateForm(request.POST,instance=shop)
        bound_form_p=ShopProductUpdateForm(request.POST)
        query=[(p.title,p.title) for p in shop.products.all()]
        query_add=[(p.title,p.title) for p in Product.objects.all() if p not in shop.products.all()]
        pr_del=Product.objects.filter(title__in=bound_form_p['products'].value())
        pr_add=Product.objects.filter(title__in=bound_form_p['products_add'].value())
        
        new_prods=[p.title for p in shop.products.all() if p.title not in bound_form_p['products'].value()]
        new_prods.extend(bound_form_p['products_add'].value())
        
        
        context={'form':bound_form,
                 'shop':shop,
                 #'s':(new_prods,pr_del, pr_add,bound_form_p['products_add'].value()),
                 'products':bound_form_p['products'].as_widget(forms.CheckboxSelectMultiple(choices=query)),
                 'products_add':bound_form_p['products_add'].as_widget(forms.CheckboxSelectMultiple(choices=query_add))}
        if bound_form.is_valid():
            new_shop=bound_form.save()
            new_shop.products.set(Product.objects.filter(title__in=new_prods))
            new_shop.save()
            return redirect(new_shop)
        else:
            return render(request, 'products/shop_update.html',context=context)

