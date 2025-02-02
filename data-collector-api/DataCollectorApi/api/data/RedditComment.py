from bson import ObjectId


class RedditComment:
    def __init__(self, post_id, text, created_at, score, is_submitter, keywords=None, location=None, latitude=None, longitude=None, comment_id=None):
        self._id = comment_id if comment_id else ObjectId()
        self.post_id = post_id
        self.text = text
        self.created_at = created_at
        self.score = score
        self.is_submitter = is_submitter
        self.keywords = keywords or []  
        self.location = location 
        self.latitude = latitude  
        self.longitude = longitude 

    def __repr__(self):
        return f'<Comment {self._id}>'

    def __dict__(self):
        return {
            "_id": self._id,
            "post_id": self.post_id,
            "text": self.text,
            "created_at": self.created_at,
            "score": self.score,
            "is_submitter": self.is_submitter,
            "keywords": self.keywords,
            "location": self.location,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            comment_id=data.get("comment_id"),
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

    @property
    def id(self):
        return self._id
