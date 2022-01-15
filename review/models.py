from django.db import models
from django.contrib.auth.models import User
from products.models import Product


SCORE_CHOICES = [
                (1, '★'),
                (2, '★★'),
                (3, '★★★'),
                (4, '★★★★'),
                (5, '★★★★★'),
                ]


class Review(models.Model):
    product = models.ForeignKey(
                        Product,
                        on_delete=models.CASCADE,
                        related_name='review')
    comment = models.TextField(max_length=255)
    rating = models.PositiveSmallIntegerField(
                                            null=True,
                                            default=3,
                                            choices=SCORE_CHOICES
                                            )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.product.name + '-' + str(self.user.username)

    def get_percent(self):
        percent = round(self.score / 5 * 100)
        return percent
