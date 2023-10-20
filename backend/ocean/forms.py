from django import forms


class ObservationForm(forms.Form):
    obsCode = forms.CharField(label='관측소 코드')
    date = forms.CharField(label="날짜", help_text='날짜형식:YYYYMMDDHH')

    def clean_data(self):
        date = self.cleaned_data['date']
        if not date.isdigit() or len(date) != 10:
            raise forms.ValidationError('날짜 형식은 YYYYMMDDHH여야 합니다.')
        return date
