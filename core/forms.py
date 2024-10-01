from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Habitacion, Reserva, Empleado

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente_nombre', 'cliente_apellidos', 'cliente_email', 'cliente_telefono']

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['habitacion_numero', 'habitacion_categoria', 'habitacion_descripcion', 'habitacion_precio', 'hotel']

# class ReservaForm(forms.ModelForm):
#     class Meta:
#         model = Reserva
#         fields = ['reserva_fecha', 'reserva_fecha_inicio', 'reserva_fecha_fin', 'reserva_total_dias', 'reserva_estado', 'cliente', 'habitacion']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['empleado_nombre', 'empleado_apellidos', 'empleado_rol', 'empleado_email', 'empleado_telefono', 'usuario']

