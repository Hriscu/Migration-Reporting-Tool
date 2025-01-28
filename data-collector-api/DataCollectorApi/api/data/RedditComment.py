from bson import ObjectId


class RedditComment:
    def __init__(self, post_id, text, created_at, score, is_submitter, comment_id=None):
        self._id = comment_id if comment_id else ObjectId()
        self.post_id = post_id
        self.text = text
        self.created_at = created_at
        self.score = score
        self.is_submitter = is_submitter

    def __repr__(self):
        return f'<Comment {self._id}>'

    def __dict__(self):
        return {
            "_id": self._id,
            "post_id": self.post_id,
            "text": self.text,
            "created_at": self.created_at,
            "score": self.score,
            "is_submitter": self.is_submitter
        }

    @classmethod
    def from_dict(cls, data):
        """Create a RedditComment instance from a MongoDB document."""
        return cls(
            comment_id=data.get("comment_id"),
            post_id=data.get("post_id"),
            text=data.get("text"),
            created_at=data.get("created_at"),
            score=data.get("score"),
            is_submitter=data.get("is_submitter")
        )

    @property
    def id(self):
        return self._id
