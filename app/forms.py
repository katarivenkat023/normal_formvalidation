from django import forms

def chaeck_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError("not valid")


def lenght(value):
    if len(value)<6:
        raise forms.ValidationError("not valid")
    
    

 
 
        
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[chaeck_for_a,lenght])
    age=forms.IntegerField()
    email=forms.EmailField(validators=[chaeck_for_a])