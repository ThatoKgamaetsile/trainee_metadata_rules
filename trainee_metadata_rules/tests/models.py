from django.db import models
from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class ListModel(ListModelMixin, BaseUuidModel):
    pass


class ResultsToRecord(ListModelMixin, BaseUuidModel):

    name = models.CharField(
        verbose_name='Name',
        max_length=250,
    )

    class Meta:
        app_label = 'trainee_metadata_rules'
