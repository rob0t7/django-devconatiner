import datetime

from typing import Optional, TYPE_CHECKING
from django.db import models
from django.utils import timezone

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager


class Question(models.Model):
    """
    Question model.
    """

    id = models.AutoField(primary_key=True)
    if TYPE_CHECKING:
        choice_set = RelatedManager["Choice"]()
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return str(self.question_text)

    def was_published_recently(self) -> bool:
        now = timezone.now()
        return (
            timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now
        )


class Choice(models.Model):
    """
    Valid choices for a specific Question.
    """

    question_id: Optional[int]
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.choice_text)
