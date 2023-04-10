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

class Music(models.Model):
    title = models.CharField("Título", max_length=150)
    content = models.TextField(
        "Conteúdo"
    )
    singer = models.ForeignKey(Singer, verbose_name="Cantor", on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Musica"
        verbose_name_plural = "Musicas"
        indexes = [
            GinIndex(
                SearchVector("title", "singer__name", "content", config="portuguese"),
                name="search_vector_idx",
            )
        ]

class Feat(models.Model):
    music = models.ForeignKey(Music, verbose_name="Musica", related_name="feats", on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, verbose_name="Cantor", on_delete=models.CASCADE)

    def __str__(self):
        return "Feat of %s in %s" % (str(self.singer), str(self.music))
    
    class Meta:
        verbose_name = "Participação Música"
        verbose_name_plural = "Participações Músicas"
