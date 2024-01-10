from rest_framework import serializers
from .models import News, Comment, Report

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'datetime']
        read_only_fields = ['id','datetime']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'news', 'user', 'text', 'datetime']
        read_only_fields = ['id', 'user', 'datetime']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not self.context['request'].user.is_staff:
            representation.pop('user', None)
        return representation

class ReportSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Report
        fields = ['id', 'news', 'comment', 'user']
        extra_kwargs = {'user': {'write_only': True}}

