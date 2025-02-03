from rest_framework import generics, status
from rest_framework.response import Response
from .models import RedditPost
from .serializers import RedditPostSerializer
from rest_framework.permissions import IsAuthenticated

class RedditPostListView(generics.ListCreateAPIView):
    queryset = RedditPost.objects.all()
    serializer_class = RedditPostSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        posts = self.queryset.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedditPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RedditPost.objects.all()
    serializer_class = RedditPostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = '_id'
