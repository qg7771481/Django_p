from django.db import models


class StudentGroup(models.Model):
    number = models.CharField(max_length=20, verbose_name="Номер групи")
    slogan = models.CharField(max_length=200, blank=True, verbose_name="Гасло")
    meeting_room = models.CharField(max_length=50, verbose_name="Кабінет зборів")

    def __str__(self):
        return self.number


class LibraryCard(models.Model):
    card_number = models.CharField(max_length=50, unique=True, primary_key=True, verbose_name="Номер читацького квитка")
    issue_date = models.DateField(auto_now_add=True, verbose_name="Дата видачі")
    expiration_date = models.DateField(verbose_name="Дата закінчення")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return f"Картка {self.card_number}"


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    student_ticket_number = models.CharField(max_length=20, unique=True, verbose_name="Номер студентського")
    email = models.EmailField(verbose_name="Пошта")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")

    group = models.ForeignKey(
        StudentGroup,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    library_card = models.OneToOneField(
        LibraryCard,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='student_owner'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Literature(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    publish_date = models.DateField(verbose_name="Дата видання")
    year = models.PositiveIntegerField(verbose_name="Рік")
    isbn = models.CharField(max_length=13, unique=True, blank=True, verbose_name="ISBN")

    def __str__(self):
        return f"{self.title} ({self.year})"


class BorrowingProcess(models.Model):
    library_card = models.ForeignKey(
        LibraryCard,
        on_delete=models.CASCADE,
        related_name='borrowed_books'
    )

    book = models.ForeignKey(
        Literature,
        on_delete=models.CASCADE,
        related_name='borrowing_history'
    )

    borrow_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата взяття")
    return_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата повернення")
    librarian_name = models.CharField(max_length=100, verbose_name="Хто видав (ПІБ)")

    def __str__(self):
        return f"{self.book.title} -> Картка {self.library_card.id}"