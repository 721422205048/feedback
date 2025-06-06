from django import forms

#form class

class ReviewsForm(forms.Form):
    user_name= forms.CharField(label="your name", max_length=5)
    review_text =forms.CharField(label="feedback",widget=forms.Textarea)
    rating =forms.IntegerField(label="your Rating",min_value=1,max_value=5)