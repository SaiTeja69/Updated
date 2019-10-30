from django import forms
from .models import post



class PostModelForm(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','slug','image','description']

    def clean_title(self,*args,**kwargs):
        #take the instance
        instance=self.instance
        #take title to check
        #and get q set
        title=self.cleaned_data.get('title')
        qs=post.objects.filter(title__iexact=title)
        #if instance is not none or not taken remove from current set
        if instance is not None:
            qs=qs.exclude(pk=instance.pk)
            #if something left raise error
        if qs.exists():
            raise forms.ValidationError('already taken please select new one')
        return title
