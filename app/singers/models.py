from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector

class Singer(models.Model):
    name = models.CharField("Cantor", max_length=150)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Cantor"
        verbose_name_plural = "Cantores"
        indexes = [
            GinIndex(
                SearchVector("name", config="portuguese"),
                name="singer_search_vector_idx",
            )
        ]
