from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator


class PersonalInfo(models.Model):
    fname = models.CharField(max_length=50, verbose_name='First Name')
    lname = models.CharField(max_length=50, verbose_name='Last Name')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    photo = models.ImageField(upload_to='media/images/', verbose_name='Profile Picture')
    birthdate = models.DateField(verbose_name='Birth Date')
    job_title = models.CharField(max_length=50, verbose_name='Job Title')
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    about = RichTextField(verbose_name='About Me')
    pdfCV = models.FileField(upload_to='media/pdfs/', verbose_name='PDF CV',
                             validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    logo = models.ImageField(upload_to='media/logo/', verbose_name='Logo')
    availability = models.CharField(
        max_length=20,
        choices=[('available', 'Available'), ('not_available', 'Not Available')],
        default='available'
    )

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company if self.company else 'N/A'}"


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True, null=True)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    date_given = models.DateField()

    def __str__(self):
        return f"Testimonial from {self.name}"


class Banner(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('projects', 'Projects'),
        ('skills', 'Skills'),
        ('contact', 'Contact'),
    ]

    page = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    image = models.ImageField(upload_to='banners/')
    alt_text = models.CharField(max_length=255, help_text="Alternative text for the banner image")

    def __str__(self):
        return f"Banner for {self.get_page_display()}"
