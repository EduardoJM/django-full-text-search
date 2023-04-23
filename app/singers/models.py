from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    TrigramSimilarity,
)

class SingerManager(models.Manager):
    def search(self, term):
        if not term:
            return self.annotate(
                rank=models.Value(0),
                similarity=models.Value(0)
            ).all()
        vector = SearchVector("name", config="portuguese")
        query = SearchQuery(term, config="portuguese")
        return self.annotate(
            search=vector,
            rank=SearchRank(vector, query),
            similarity=TrigramSimilarity("name", term),
        ).filter(
            models.Q(search=query) | models.Q(similarity__gt=0)
        ).order_by("-rank", "-similarity").all()

class Singer(models.Model):
    name = models.CharField("Cantor", max_length=150)

    objects = SingerManager()
    
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
