from bson import ObjectId


class RedditPost:
    def __init__(self, title, content, text, subreddit, created_at, score, num_comments, is_self, url, keywords=None, location=None, latitude=None, longitude=None, media_urls=None, post_id=None):
        self._id = post_id if post_id else ObjectId()
        self.title = title
        self.content = content
        self.text = text
        self.subreddit = subreddit
        self.created_at = created_at
        self.score = score
        self.num_comments = num_comments
        self.is_self = is_self
        self.url = url
        self.keywords = keywords or [] 
        self.location = location 
        self.latitude = latitude  
        self.longitude = longitude  
        self.media_urls = media_urls or []  

    def __repr__(self):
        return f'<Post {self._id}>'

    @classmethod
    def from_dict(cls, data):
        """Create a RedditPost instance from a MongoDB document."""
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

    def __str__(self):
        return (f"""Post: {self._id}\n"""
                f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Text: {self.text}\n"
                f"Subreddit: {self.subreddit}\n"
                f"Created At: {self.created_at}\n"
                f"Score: {self.score}\n"
                f"Number of Comments: {self.num_comments}\n"
                f"Is Self: {self.is_self}\n"
                f"URL: {self.url}\n"
                f"Keywords: {self.keywords}\n"
                f"Location: {self.location}\n"
                f"Latitude: {self.latitude}\n"
                f"Longitude: {self.longitude}\n"
                f"Media URLs: {self.media_urls}\n")

    def __dict__(self):
        return {
            "_id": self._id,
            "title": self.title,
            "content": self.content,
            "text": self.text,
            "subreddit": self.subreddit,
            "created_at": self.created_at,
            "score": self.score,
            "num_comments": self.num_comments,
            "is_self": self.is_self,
            "url": self.url,
            "keywords": self.keywords,
            "location": self.location,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "media_urls": self.media_urls
        }

    def __eq__(self, other):
        if not isinstance(other, RedditPost):
            return False

        return self.__dict__() == other.__dict__()

    @property
    def id(self):
        return self._id
