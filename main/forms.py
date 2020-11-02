# from django import forms 
# from . models import Employee

# class EmployeeForm(forms.ModelForm):
    
#     class Meta:
#         model = Employee
#         fields = '__all__'
#         labels = {
#             'fullname': 'Full Name',
#             'emp_code': 'Emp Code',
#         }

#     def __init__(self, *args, **kwargs):
#         super(EmployeeForm, self).__init__(*args, **kwargs) 
#         self.fields['gender'].empty_label = 'Select'
#         self.fields['status'].empty_label = 'Select'
#         self.fields['citizenship_number'].required = False
#         self.fields['home_phone_number'].required = False
#         self.fields['department'].required = False
#         self.fields['image'].required = False
#         self.fields['bio'].required = False
        
