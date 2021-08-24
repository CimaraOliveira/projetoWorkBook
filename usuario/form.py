from django.forms import ModelForm, forms
from usuario.models import Profissional, Usuario
from django.core.exceptions import ValidationError

class FormPerfil(ModelForm):
    class Meta:
        model = Profissional
        fields = ['profissao', 'categoria', 'imagem','descricao']
        exclude = ('slug','user',)

    def clean_user_id(self):
            slug = self.cleaned_data['slug']
            if slug:
                profissional = Profissional.objects.filter(slug=slug).exists()
                if profissional:
                    raise ModelForm.ValidationError('Existe')
                return slug

class FormDadosPessoais(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ('is_active','is_staff','is_superuser','user_permissions','groups','last_login','password','status', 'date_joined',)

class FormEditProfissional(ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'
        exclude = ('user','slug',)



