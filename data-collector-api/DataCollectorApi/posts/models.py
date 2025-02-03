from django.db import models
from bson import ObjectId

class RedditPost(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    title = models.CharField(max_length=255)
    content = models.TextField()
    text = models.TextField()
    subreddit = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    score = models.IntegerField()
    num_comments = models.IntegerField()
    is_self = models.BooleanField(default=False)
    url = models.URLField()
    keywords = models.JSONField(default=list, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    media_urls = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Post {self._id}"
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            post_id=data.get("post_id"),
            title=data.get("title"),
            content=data.get("content"),
            text=data.get("text"),
            subreddit=data.get("subreddit"),
            created_at=data.get("created_at"),
            score=data.get("score"),
            num_comments=data.get("num_comments"),
            is_self=data.get("is_self"),
            url=data.get("url"),
            keywords=data.get("keywords"),
            location=data.get("location"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            media_urls=data.get("media_urls")
        )
