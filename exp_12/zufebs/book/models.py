from django.db import models


# Create your models here.
class t_book(models.Model):
    book_name = models.CharField(null=False, max_length=20)
    book_pic = models.ImageField(upload_to='static/book_images/')
    book_author = models.CharField(max_length=50)
    book_price = models.FloatField()
    book_info = models.TextField()
    book_isbn = models.CharField(max_length=15)
    book_press = models.CharField(max_length=30)
    book_date = models.DateField()
    book_num = models.IntegerField(default=10)

    def __str__(self):
        return self.book_name + ' | ' + self.book_author[:10] + '...| '


def get_all_book():
    return t_book.objects.all()


def get_book_by_time():
    return t_book.objects.order_by('book_date')


def search_book(bname):
    return t_book.objects.filter(book_name=bname)
