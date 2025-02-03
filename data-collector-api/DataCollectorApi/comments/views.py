from rest_framework import generics, status
from rest_framework.response import Response
from .models import RedditComment
from .serializers import RedditCommentSerializer
from rest_framework.permissions import IsAuthenticated

class RedditCommentListView(generics.ListCreateAPIView):
    queryset = RedditComment.objects.all()
    serializer_class = RedditCommentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        comments = self.queryset.filter(post_id=kwargs['post_id'])
        serializer = self.serializer_class(comments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedditCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RedditComment.objects.all()
    serializer_class = RedditCommentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = '_id'
