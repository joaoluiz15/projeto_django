from django.shortcuts import render

# Create your views here.

from catalogo.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all() # Get 5 books containing the title war
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book
   # book = Book.objects().all().order_by('name').values()

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    queryset = Book.objects.all()
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author
    # author = Author.objects().all().order_by('name').values()
