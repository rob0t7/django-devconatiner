import graphene
from graphene_django import DjangoObjectType

from .models import Question, Choice


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date", "choice_set")


class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice
        fields = ("choice_text", "votes")


class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)

    def resolve_questions(_root, _info):
        return Question.objects.all()


class QuestionMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        id = graphene.ID()

    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, text, id):
        question = Question.objects.get(pk=id)
        question.question_text = text
        question.save()
        return QuestionMutation(question=question)


class ChoiceVoteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, id):
        choice = Choice.objects.get(pk=id)
        choice.votes += 1
        choice.save()
        return QuestionMutation(question=choice.question)


class Mutation(graphene.ObjectType):
    update_question = QuestionMutation.Field()
    vote = ChoiceVoteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
