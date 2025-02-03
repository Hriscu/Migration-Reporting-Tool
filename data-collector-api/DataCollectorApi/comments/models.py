from django.db import models
from bson import ObjectId

class RedditComment(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    post_id = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField()
    score = models.IntegerField()
    is_submitter = models.BooleanField(default=False)
    keywords = models.JSONField(default=list, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Comment {self._id}"
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            post_id=data.get("post_id"),
            text=data.get("text"),
            created_at=data.get("created_at"),
            score=data.get("score"),
            is_submitter=data.get("is_submitter"),
            keywords=data.get("keywords"),
            location=data.get("location"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude")
        )
