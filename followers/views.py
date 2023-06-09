from .models import Follower
from rest_framework import generics, permissions
from .serializers import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user'.
    Create a follower, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a follower.
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowedByList(generics.ListCreateAPIView):
    """
    Used to test the passing of a followed by attribute to filter against
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        user = self.kwargs['owner']
        return Follower.objects.filter(owner__username=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowingList(generics.ListCreateAPIView):
    """
    Used to test the passing of a following attribute to filter against
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        followed_name = self.kwargs['followed_name']
        return Follower.objects.filter(followed__username=followed_name)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    No Update view, as we either follow or unfollow users
    Destroy a follower, i.e. unfollow someone if owner
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    queryset = Follower.objects.all()
