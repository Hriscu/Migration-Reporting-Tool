from rest_framework import serializers
from .models import RedditComment

class RedditCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditComment
        fields = ['_id', 'post_id', 'text', 'created_at', 'score', 'is_submitter', 'keywords', 'location', 'latitude', 'longitude']

    def create(self, validated_data):
        return RedditComment.objects.create(**validated_data)
