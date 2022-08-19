from django.db.models import Q
from rest_framework.generics import (
  ListAPIView, CreateAPIView,
  RetrieveUpdateAPIView,
  RetrieveAPIView,
  DestroyAPIView
)
from rest_framework import pagination
from rest_framework.permissions import (
 IsAuthenticatedOrReadOnly
)
from ...core.pagination import PostLimitOffsetPagination
from .serializers import TABLE, TimeLogSerializer, TimeLogCreateSerializer


class TimeLogListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TimeLogSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = TABLE.objects.all()

        page_size_key = 'page_size'
        page_size = self.request.GET.get(page_size_key)
        query = self.request.GET.get('q')
        pagination.PageNumberPagination.page_size = page_size if page_size else 10

        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        return queryset_list.order_by('-id')


class TimeLogCreateAPIView(CreateAPIView):
    serializer_class = TimeLogCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TABLE.objects.all()


class TimeLogDetailAPIView(RetrieveAPIView):
    queryset = TABLE.objects.all()
    serializer_class = TimeLogSerializer


class TimeLogDeleteAPIView(DestroyAPIView):
    queryset = TABLE.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TimeLogSerializer


class TimeLogUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TABLE.objects.all()
    serializer_class = TimeLogSerializer
