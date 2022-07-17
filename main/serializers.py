from rest_framework import serializers
from .models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'text', 'published', 'count',  'created')


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    author = serializers.CharField()
    text = serializers.CharField()
    published = serializers.CharField(max_length=4)
    count = serializers.IntegerField()
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.text = validated_data.get('text', instance.text)
        instance.published = validated_data.get('published', instance.published)
        instance.count = validated_data.get('count', instance.count)
        instance.save()
        return instance


class BookSerializerAuto(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Book
        fields = '__all__'
        # fields = ('title', 'author', 'text')