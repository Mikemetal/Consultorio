from django.db import models
from django.forms import ModelForm

class Paciente(models.Model):
	Nombre = models.CharField(max_length=50)
	FechaCreacion = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.Nombre

class PacienteForm(ModelForm):
	class Meta:
		model = Paciente

class Agenda(models.Model):
	PacienteID = models.ForeignKey(Paciente)
	Descripcion = models.CharField(max_length=50)
	Fecha = models.DateField()
	HoraInicio = models.TimeField()
	HoraFinal = models.TimeField()
	Asistio = models.BooleanField()
	Cancelada = models.BooleanField()
	
	def __unicode__(self):
		return self.Descripcion

class AgendaForm(ModelForm):
	class Meta:
		model = Agenda
