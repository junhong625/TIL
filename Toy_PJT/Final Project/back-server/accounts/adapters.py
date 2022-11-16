from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: nickname
        print(data)
        nickname = data.get('nickname')
        print(nickname)
        # if nickname:
        user.nickname = 'kaka'
        user.save()

        return user