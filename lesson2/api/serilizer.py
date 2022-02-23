
from rest_framework import serializers
from blog.models import Blog


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "author",
            "titile",
            "desc",
        )



