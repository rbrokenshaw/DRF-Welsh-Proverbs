from django_elasticsearch_dsl import Document, fields, Index

from .models import Proverb

proverb_index = Index('proverbs')

proverb_index.settings(number_of_shards=1, number_of_replicas=0)


@proverb_index.doc_type
class ProverbDocument(Document):
    class Django:
        model = Proverb
        fields = [
            'welsh',
            'english',
        ]

    def get_queryset(self):
        return super().get_queryset()
