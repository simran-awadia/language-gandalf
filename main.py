import json
import os
import re
from dataclasses import dataclass
from functools import partial
from string import Template

import g4f

from proficiency_levels import Novice, Intermediate, Champion, ProficiencyLevel
from utils import strtobool

PROFICIENCY_LEVELS = [Novice, Intermediate, Champion]
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTION_PROMPT_TEMPLATE_PATH = f"{ROOT_DIR}/prompt_resources/question_prompt.txt"


@dataclass
class ProficiencyTest:
    text: str
    question: float


def is_valid_user_input(user_input):
    return user_input and len(user_input.split()) <= 20


def display_test_question(test: ProficiencyTest):
    print(f"Your text is: {test.text}")
    print(f"Your question is: {test.question}")


def display_game_finalization(proficiency_level: ProficiencyLevel):
    print(
        f"Good game, you're a true {proficiency_level.name}! {proficiency_level.skill_level_description}"
    )


def display_game_introduction():
    print(
        "Welcome or should say bonjour à tous! Are you a novice, intermediate, or a champion French speaker? Answer "
        "these questions to find out! *Remember* all answers should be less than 20 words in length. "
    )


def game_play():
    display_game_introduction()
    system_prompt = (
        "You are a linguistic assistant who is creating a french language assessment. There are 3 "
        "levels: novice, intermediate and champion. Generate questions only in French. Use a storyteller tone."
    )

    with open(QUESTION_PROMPT_TEMPLATE_PATH) as f:
        question_prompt_template = Template(f.read())

    chat_completion = partial(
        g4f.ChatCompletion.create, model="gpt-3.5-turbo", provider=g4f.Provider.You
    )
    user_proficiency_level = Novice

    for proficiency_level in PROFICIENCY_LEVELS:
        question_prompt = question_prompt_template.substitute(
            proficiency_level=proficiency_level.name,
            source=proficiency_level.source,
            example_test=proficiency_level.example_test,
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question_prompt},
        ]

        test_question_str = chat_completion(messages=messages)
        print(test_question_str)

        # The model tends to add extra spaces or text like "Here is the JSON" so
        # regex matching is safer than using json.loads
        text_match = re.search(
            r"text[\'|\"]:\s*.?[\'|\"](.*?)[\'|\"],\s*.?[\'|\"]question", test_question_str
        ).group(1)
        question_match = re.search(
            r"question[\'|\"]:\s*.?[\'|\"](.*?)[\'|\"]\s*}", test_question_str
        ).group(1)

        display_test_question(ProficiencyTest(text=text_match, question=question_match))

        user_answer = input("Answer:")
        if not is_valid_user_input(user_answer):
            print("All answers must be less than 20 words and alphanumeric. Try again!")
            break

        messages.extend(
            [
                {"role": "assistant", "content": test_question_str},
                {
                    "role": "user",
                    "content": f"Is the correct answer: {user_answer}? Respond only with 1 word either 'True' or 'False'",
                },
            ]
        )
        is_correct_answer_str = chat_completion(messages=messages)
        is_correct_answer = strtobool(is_correct_answer_str)

        if is_correct_answer:
            print(f"Great job! You've passed the {proficiency_level.name} level.")
            user_proficiency_level = proficiency_level
        else:
            print(
                "Uh oh that's not the right answer :( Try again after some more practice."
            )
            break

    display_game_finalization(user_proficiency_level)


if __name__ == "__main__":
    game_play()
