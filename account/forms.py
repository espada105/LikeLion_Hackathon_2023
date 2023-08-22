from django import forms
from .models import User
from argon2 import PasswordHasher, exceptions


# widget은 <form> 태그의 type에 관한 부분이다.
# []input을 사용하였으면 <form>태그의 속성들을 지정하는 곳이다.
# class, id, placeholder 등을 지정할 수 있고 css로 디자인을 변경해야 할 경우 여기서 변경

class RegisterForm(forms.ModelForm):
    user_id = forms.CharField(
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'box int_id',
                'placeholder':'아이디'
            }
        ),
        error_messages={'required' : '아이디를 입력해주세요.',
                        'unique' : '중복된 아이디입니다.'}
    )
    user_pw = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'box int_pass',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )
    user_pw_confirm = forms.CharField(
        label='비밀번호 재확인',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'box int_pass_check',
                'placeholder' : '비밀번호 확인'
            }
        ),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )
    user_name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'box int_name',
                'placeholder' : '이름'
            }
        ),
        error_messages={'required' : '닉네임을 입력해주세요.'}
    )
    user_email = forms.EmailField(
        label='이메일',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'box int_email',
                'placeholder' : '이메일'
            }
        ),
        error_messages={'required' : '이메일을 입력해주세요.'}
    )
    user_phone = forms.CharField( 
        label='전화번호',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'box int_mobile',
                'placeholder':'전화번호'
            }
        ),
        error_messages={'required' : '전화번호를 입력해주세요.'}
    )
    GENDER_CHOICES = (
        ('M', '남성'),
        ('F', '여성'),
        ('O', '기타'),
    )

    user_gender = forms.ChoiceField(
        label='성별',
        choices=GENDER_CHOICES,
        required=True,
        widget=forms.Select(
            attrs={
                'class':'box gender_code',
                'placeholder':'성별'
            }
        ),
        error_messages={'required' : '성별을 입력해주세요.'}
    )
    # 필드 순서를 지정하는 field_order
    field_order =[
        'user_id',
        'user_pw',
        'user_pw_confirm',
        'user_name',
        'user_gender',
        'user_email',
        'user_phone'
    ]

    class Meta:
        model = User
        fields = [
            'user_id',
            'user_pw',
            'user_name',
            'user_gender',
            'user_email',
            'user_phone'
        ]

    # 유효성 검사에 필요한 clean함수
    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')
        user_pw_confirm = cleaned_data.get('user_pw_confirm', '')
        user_name = cleaned_data.get('user_name', '')
        user_email = cleaned_data.get('user_email', '')
        user_phone = cleaned_data.get('user_phone','')
        user_gender = cleaned_data.get('user_gender','')

        if user_pw != user_pw_confirm:
            return self.add_error('user_pw_confirm','비밀번호가 다릅니다.')
        elif not (4<= len(user_id)<=16):
            return self.add_error('user_id', '아이디는 4~16자로 입력해 주세요.')
        elif 8 > len(user_pw):
            return self.add_error('user_pw','비밀번호는 8자 이상으로 적어주세요.')
        else:
            self.user_id = user_id
            self.user_pw = PasswordHasher().hash(user_pw)
            self.user_pw_confirm = user_pw_confirm
            self.user_name = user_name
            self.user_email = user_email
            self.user_phone = user_phone
            self.user_gender = user_gender



# ################################################################################
# login
class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=32,
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'box int_id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required' : '아이디를 입력해주세요. '}
    )
    user_pw = forms.CharField(
        max_length=128,
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'box int_pass',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={
            'required' : '비밀번호를 입력해주세요. '}
    )

    field_order = [
        'user_id',
        'user_pw',
    ]

    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')

        if user_id == '':
            return self.add_error('user_id','아이디를 다시 입력해 주세요.')
        elif user_pw =='':
            return self.add_error('user_pw','비밀번호를 다시 입력해 주세요.')
        else:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return self.add_error('user_id','아이디가 존재하지 않습니다. ')
            
            try:
                PasswordHasher().verify(user.user_pw, user_pw)
            except exceptions.VerifyMismatchError:
                return self.add_error('user_pw','비밀번호가 다릅니다.')
            
            self.login_session = user.user_id

        