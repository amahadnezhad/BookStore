from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from books.models import Book


class Cart:
    def __init__(self, request):
        """
            Initialize The Cart
        """
        # Save User Request
        self.request = request
        self.session = request.session

        # Getting Cart From Session
        cart = self.session.get('cart')

        # If User Doesn't have Cart , Create a New One
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, book, quantity=1, replace_current_quantity=False):
        """
            Add The Specified Book To The Cart If It Exists
        """
        book_id = str(book.id)

        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity

        messages.success(self.request, _('Book Successfully Added To Cart'))
        self.save()

    def remove(self, book):
        """
            Remove A Product From The Cart
        """
        book_id = str(book.id)

        if book_id in self.cart:
            del self.cart[book_id]
            messages.success(self.request, _('Book Successfully Removed From Cart'))
            self.save()

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)

        cart = self.cart.copy()

        for book in books:
            cart[str(book.id)]['book_obj'] = book

        for item in cart.values():
            item['total_price'] = item['book_obj'].price * item['quantity']
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        book_ids = self.cart.keys()

        return sum(item['quantity'] * item['book_obj'].price for item in self.cart.values())

    def save(self):
        """
            Mark Sessions As Modified To Save Changes
        """
        self.session.modified = True
