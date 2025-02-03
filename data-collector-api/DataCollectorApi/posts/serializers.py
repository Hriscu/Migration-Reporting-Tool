from rest_framework import serializers
from .models import RedditPost

class RedditPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditPost
        fields = ['_id', 'title', 'content', 'text', 'subreddit', 'created_at', 'score', 'num_comments', 'is_self', 'url', 'keywords', 'location', 'latitude', 'longitude', 'media_urls']

    def create(self, validated_data):
        return RedditPost.objects.create(**validated_data)
