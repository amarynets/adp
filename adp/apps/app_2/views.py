from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView

from apps.app_1.models import Book


def ping(request):
    return JsonResponse({'ping': 'pong'})


class BooksRelatedView(ListView):
    model = Book
    template_name = 'app_2/book_related_view.html'
    context_object_name = 'book_list'
