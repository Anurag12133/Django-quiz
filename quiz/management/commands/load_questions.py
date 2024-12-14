from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Load quiz questions into the database'

    def handle(self, *args, **kwargs):
        questions = [
        {
        "question": "A flashing red traffic light signifies that a driver should do what?",
        "A": "stop",
        "B": "speed up",
        "C": "proceed with caution",
        "D": "honk the horn",
        "answer": "A"
        }, {
        "question": "A knish is traditionally stuffed with what filling?",
        "A": "potato",
        "B": "creamed corn",
        "C": "lemon custard",
        "D": "raspberry jelly",
        "answer": "A"
        }, {
        "question": "A pita is a type of what?",
        "A": "fresh fruit",
        "B": "flat bread",
        "C": "French tart",
        "D": "friend bean dip",
        "answer": "B"
        }, {
        "question": "A portrait that comically exaggerates a person's physical traits is called a what?",
        "A": "landscape",
        "B": "caricature",
        "C": "still life",
        "D": "Impressionism",
        "answer": "B"
        }, {
        "question": "A second-year college student is usually called a what?",
        "A": "sophomore",
        "B": "senior",
        "C": "freshman ",
        "D": "junior ",
        "answer": "A"
        }
        ]

        for question in questions:
            Question.objects.update_or_create(
                question_text=question["question"],
                defaults={
                    "option_a": question["A"],
                    "option_b": question["B"],
                    "option_c": question["C"],
                    "option_d": question["D"],
                    "answer": question["answer"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Questions loaded successfully!"))
