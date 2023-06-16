# construct_with_gpt4

A helper function to parse GPT's output into your own data model with minimal boilerplate code.

## Usage Example

```py
from pydantic import BaseModel, Field

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
recipe = construct_with_gpt4(Recipe, dish='spagehtti bolognese')

print(recipe.json())
# prints { "ingredients": [{ "name": "spaghetti", "unit": "grams", ... }, ...], ... }
```

## How it works

1. With the help of [Pydantic](https://docs.pydantic.dev/latest/usage/schema/), the data model is converted to a JSON Schema.
2. The JSON Schema is then passed to GPT-4, along with the other function parameters ("dish" in the example above).
3. GPT-4 returns a JSON result which is used to instantiate the data model class.

## Status

This is a proof of concept. Use at your own risk. PRs are welcome.
