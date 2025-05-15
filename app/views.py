from symtable import Class

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction


class HomeView(APIView):
    def get(self, request):
        transactions = Transaction.objects.select_related('status', 'kind', 'category', 'sub_category')
        result = []

        for t in transactions:
            result.append({
                'created_at': t.created_at,
                'status': t.status.name if t.status else None,
                'kind': t.kind.name if t.kind else None,
                'category': t.category.name if t.category else None,
                'sub_category': t.sub_category.data if t.sub_category else None,
                'amount': t.amount,
                'note': t.note
            })

        return Response({"main_data": result})

