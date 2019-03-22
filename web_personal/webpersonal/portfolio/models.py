from django.db import models

# Create your models here.
class Project(models.Model):
    tittle = models.CharField(max_length=200, verbose_name="Tirulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="project")
    link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")
    

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]        
        
    def __str__(self):
        return self.tittle