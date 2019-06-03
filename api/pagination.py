from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'size'
    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'total_pages': self.page.paginator.num_pages,
            'total_itens': self.page.paginator.count,
            'current_page': self.page.number,
            'current_page_size': len(data),
            'has_previous': self.page.has_previous(),
            'has_next': self.page.has_next(),
            'results': data
        })
