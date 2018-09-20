from rest_framework.pagination import PageNumberPagination

# pagination class 생성
class PostPageNumberPagination(PageNumberPagination):
    page_size = 3
