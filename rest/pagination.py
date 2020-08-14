from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 5
