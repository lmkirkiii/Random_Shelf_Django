from django import forms
from .models import Treasure, File_Treasure

class TreasureForm(forms.ModelForm):

    class Meta:
        model = Treasure
        fields = ('title', 'img_url', 'description',)

class File_TreasureForm(forms.ModelForm):
    class Meta:
        model = File_Treasure
        fields = ('title','description', 'file_path',)