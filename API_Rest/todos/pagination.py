from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'count'
    max_page_size = 10
    page_query_param = 'pag'