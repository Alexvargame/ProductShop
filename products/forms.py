from django import forms
from django.forms import fields, widgets

from .models import *


                
class CategoryCreateForm(forms.ModelForm):


    class Meta:
        model=Category
        fields=['title','description']
        widgets={
              'title':forms.TextInput(attrs={'class':'form-control','empty_value':True}),
              'description':forms.Textarea(attrs={'class':'form-control','empty_value':True}),
            }

                
class ProductCreateForm(forms.ModelForm):


    class Meta:
        model=Product
        fields=['title','amount','price','category','active','description']
        widgets={
              'title':forms.TextInput(attrs={'class':'form-control','empty_value':True}),
              'amount':forms.NumberInput(attrs={'class':'form-control','empty_value':True}),
              'price':forms.NumberInput(attrs={'class':'form-control','empty_value':True}),
              'category':forms.Select(choices=[(cat.title, cat.title) for cat in Category.objects.all()],attrs={'class':'form-control','empty_value':True}),
              'active':forms.Select(choices=[(True, True),(False, False)],attrs={'class':'form-control','empty_value':True}),
              'description':forms.Textarea(attrs={'class':'form-control','empty_value':True}),
              
            }

class ProductSelectPriceForm(forms.Form):

    min_price=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control','empty_value':True}))
    max_price=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control','empty_value':True}))

class ProductSearchForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','empty_value':True}))
       
class ShopCreateForm(forms.ModelForm):
##    image=forms.ImageField(label=u'Фотографии',
##                           widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': 'multiple', 'empty_value':True},required=False))

    class Meta:
        model=Shop
        fields=['title','description','image']
        widgets={
              'title':forms.TextInput(attrs={'class':'form-control','empty_value':True}),                           
              'image':forms.ClearableFileInput(attrs={'class':'form-control','multiple': 'multiple', 'empty_value':True,'required':False}),
              'description':forms.Textarea(attrs={'class':'form-control','empty_value':True}),
              
            }

class ShopProductCreateForm(forms.Form):

    products=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=[(p.title,p.title) for p in Product.objects.all()],
                                    attrs={'class':'form-control','empty_value':True}))
   


class ShopUpdateForm(forms.ModelForm):
      #image=forms.ImageField(label=u'Фотографии', widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': 'multiple', 'empty_value':True}))
      class Meta:
        model=Shop
        fields=['title','description']
        widgets={
              'title':forms.TextInput(attrs={'class':'form-control','empty_value':True}),                           
             
              'description':forms.Textarea(attrs={'class':'form-control','empty_value':True}),
              
            }


class ShopProductUpdateForm(forms.Form):

    products=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=[(p.title,p.title) for p in Product.objects.all()],
                                    attrs={'class':'form-control','empty_value':True}))
    products_add=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=[(p.title,p.title) for p in Product.objects.all()],
                                    attrs={'class':'form-control','empty_value':True}))

