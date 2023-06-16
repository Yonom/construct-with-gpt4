from pydantic import BaseModel, Field
from gpt_construct import construct_with_gpt4
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


# define data models

class Ingredient(BaseModel):
    name: str
    unit: str
    amount: int


class Recipe(BaseModel):
    ingredients: list[Ingredient]
    instructions: list[str]
    time_to_cook: int = Field(..., description="time to cook in minutes")


# instantiate the model with the help of GPT
recipe = construct_with_gpt4(Recipe, dish="spagehtti bolognese")

print(recipe.json())
