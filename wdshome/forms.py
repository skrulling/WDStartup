from django import forms
from django.contrib.auth.models import User
from .models import Annonser, Brukerinformasjon, Utviklere, Søknader
from django.utils.translation import ugettext_lazy as _

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': _('Brukernavn'),
            'email': _('Epost'),
            'password': _('Passord'),
        }


class AnnonseForm(forms.ModelForm):
    JAVA = 'Java'
    PHP = 'PHP'
    WORDPRESS = 'Wordpress'
    ANDROID = 'Android'
    IOS = 'iOS'
    PYTHON = 'Python'
    NET = '.NET'
    INGEN = 'Ingen'

    TAGS_CHOICES = (
        ('Java', 'Java'),
        ('PHP', 'PHP'),
        ('Wordpress', 'Wordpress'),
        ('Android', 'Android'),
        ('iOS', 'iOS'),
        ('Python', 'Python'),
        ('.NET', '.NET'),
        ('Ingen', 'Ingen'),
    )
    tags = forms.MultipleChoiceField(choices=TAGS_CHOICES, widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Annonser
        fields = ['tittel', 'tags', 'stillinger', 'info']
        labels = {
            'tittel': _('Tittel'),
            'tags': _('Teknologi'),
            'stillinger': _('Antall stillinger'),
            'info': _('Innformasjon'),
        }
        help_texts = {
            'tittel': _('f.eks: "Søker iOS app-utvikler".'),
            'tags': _('f.eks: PHP, Python etc'),
            'info': _('Kort beskrivelse av stillingen, maks 1000 tegn.'),
        },

class SortForm(forms.Form):
    JAVA = 'Java'
    PHP = 'PHP'
    WORDPRESS = 'Wordpress'
    ANDROID = 'Android'
    IOS = 'iOS'
    PYTHON = 'Python'
    NET = '.NET'


    TAGS_CHOICES = (
        ('Java', 'Java'),
        ('PHP', 'PHP'),
        ('Wordpress', 'Wordpress'),
        ('Android', 'Android'),
        ('iOS', 'iOS'),
        ('Python', 'Python'),
        ('.NET', '.NET'),

    )
    sorter = forms.MultipleChoiceField(choices=TAGS_CHOICES, widget=forms.CheckboxSelectMultiple(),)

class AddinfoForm(forms.ModelForm):

    class Meta:
        model = Brukerinformasjon
        fields = ['erfaring', 'hjemmeside', 'om_meg']
        labels = {
            'erfaring': _('Tidligere erfaring'),
            'hjemmeside': _('Hjemmeside'),
            'om_meg': _('Kort om deg selv')
        }


class UtviklerForm(forms.ModelForm):
    JAVA = 'Java'
    PHP = 'PHP'
    WORDPRESS = 'Wordpress'
    ANDROID = 'Android'
    IOS = 'iOS'
    PYTHON = 'Python'
    NET = '.NET'
    INGEN = 'Ingen'

    TAGS_CHOICES = (
        ('Java', 'Java'),
        ('PHP', 'PHP'),
        ('Wordpress', 'Wordpress'),
        ('Android', 'Android'),
        ('iOS', 'iOS'),
        ('Python', 'Python'),
        ('.NET', '.NET'),
        ('Ingen', 'Ingen'),
    )
    tags = forms.MultipleChoiceField(choices=TAGS_CHOICES, widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Utviklere
        fields = ['tittel', 'tags', 'info', 'epost']
        labels = {
            'tittel': _('Tittel'),
            'tags': _('Teknologi'),
            'info': _('Innformasjon'),
            'epost': _('Epost'),
        }
        help_texts = {
            'tittel': _('f.eks: "Søker iOS app-utvikler".'),
            'tags': _('f.eks: PHP, Python etc'),
            'info': _('Kort beskrivelse av stillingen, maks 1000 tegn.'),
        },

class SøknadForm(forms.ModelForm):

    class Meta:
        model = Søknader
        fields = ['tekst', 'epost']
        labels = {
            'tekst': _('Søknadstekst'),
            'epost': _('Din epost'),
        }