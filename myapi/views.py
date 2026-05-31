# from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
# Create your views here.

@api_view(['GET'])
def home(request):

    books = Book.objects.all()
    book_serializer = BookSerializer(books, many=True)

    authors = Author.objects.all()
    author_serializer = AuthorSerializer(authors, many=True)

    print("Books queryset:", books)
    print("Authors queryset:", authors)

    print("Serialized books:", book_serializer.data)
    print("Serialized authors:", author_serializer.data)


    # return JsonResponse({
    #     'books': book_serializer.data,
    #     'authors': author_serializer.data
    # })
    
    return Response({
        'books': book_serializer.data,
        'authors': author_serializer.data
    })


from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



    

