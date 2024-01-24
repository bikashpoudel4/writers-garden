from django_elasticsearch_dsl import Document, fields, Text
from django_elasticsearch_dsl.registries import registry
from core_apps.articles.models import Article

# from elasticsearch_dsl.connections import connections
# # Establish the connection to Elasticsearch
# connections.create_connection()

@registry.register_document
class ArticleDocument(Document):
    title = fields.TextField(attr="title")
    description = fields.TextField(attr="description")
    body = fields.TextField(attr="body")
    author_first_name = fields.TextField()
    author_last_name = fields.TextField()
    tags = fields.KeywordField()

    class Index:
        name = "articles"
        # tags = Text(multi=True)  # Use Text field for multi-values like tags
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Article
        fields = ["created_at"]

    def prepare_author_first_name(self, instance):
        return instance.author.first_name 

    def prepare_author_last_name(self, instance):
        return instance.author.last_name 
    
    def prepare_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]