from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['re_enter_email']
        n=self.cleaned_data['name']
        if e!=re and n[0]=='a':
            raise forms.ValidationError('mail is not correct')
    def checking(self):
        bt=self.cleaned_data['botcatcher']
        if len(bt)>0:
            raise forms.ValidationError('it is botcatcher data')