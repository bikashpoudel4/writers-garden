from rest_framework import serializers
from core_apps.articles.models import Article, ArticleView
from core_apps.profiles.serializers import ProfileSerializer


class TagListField(serializers.Field):
    """
    Custom serializer field for representing a list of tags.
    Converts a queryset of tags to a list of tag names.
    """

    def to_representation(self, value):
        return [tag.name for tag in value.all()]

    def to_internal_value(self, data):
        """
        Convert the incoming list of tag names to a list of tag objects.
        """
        if not isinstance(data, list):
            raise serializers.ValidationError("Expected a list of tags")

        tag_objects = []
        for tag_name in data:
            tag_name = tag_name.strip()

            if not tag_name:
                continue
            tag_objects.append(tag_name)
        return tag_objects\



class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Article model, including custom fields and methods.
    """
    author_info = ProfileSerializer(source="author.profile", read_only=True)
    banner_image = serializers.SerializerMethodField()
    estimated_reading_time = serializers.ReadOnlyField()
    tags = TagListField()
    views = serializers.SerializerMethodField()
    average_rating = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.average_rating()

    def get_views(self, obj):
        """
        Method to get the number of views for an article.
        """
        return ArticleView.objects.filter(article=obj).count()

    def get_banner_image(self, obj):
        """
        Method to get the URL of the banner image for an article.
        """
        return obj.banner_image.url

    def get_created_at(self, obj):
        """
        Method to format and return the creation date of an article.
        """
        now = obj.created_at
        fromatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return fromatted_date

    def get_updated_at(self, obj):
        """
        Method to format and return the last update date of an article.
        """
        then = obj.updated_at
        fromatted_date = then.strftime("%m/%d/%Y, %H:%M:%S")
        return fromatted_date

    def create(self, validated_data):
        """
        Method to create a new article with associated tags.
        """
        tags = validated_data.pop("tags")
        article = Article.objects.create(**validated_data)
        article.tags.set(tags)
        return article

    def update(self, instance, validated_data):
        """
        Method to update an existing article with the provided data.
        """
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.body = validated_data.get("body", instance.body)
        instance.banner_image = validated_data.get("banner_image", instance.banner_image)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        if "tags" in validated_data:
            instance.tags.set(validated_data["tags"])

        instance.save()
        return instance

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "tags",
            "estimated_reading_time",
            "author_info",
            "views",
            "description",
            "body",
            "banner_image",
            "average_rating",
            "created_at",
            "updated_at",
        ]
