from rest_framework.pagination import LimitOffsetPagination
class MyPageNumberPagination(LimitOffsetPagination):
    page_size = 5
    max_page_size = 7