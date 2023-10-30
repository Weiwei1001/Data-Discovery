import os
import requests
import json
import openai

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-07-01-preview' # this may change in the future

deployment_name='gpt-35-turbo' #This will correspond to the custom name you chose for your deployment when you deployed a model.

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Write a tagline for an ice cream shop. '
response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=10)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(start_phrase+text)


prompt = '''
I will translate your request into English, and then help you identify the problematic functional dependencies based on the provided column descriptions. Here's the translation:

"In a database's relational model, I will provide you with columns with continuous values along with their meanings and possible values. I will provide you with this format {column name, maximum value, minimum value, average value, median}:

age: continuous.
fnlwgt: continuous.
capital-gain: continuous.
capital-loss: continuous.
hours-per-week: continuous.
education-num: continuous.

Then, I will give you columns with enumerable value types in the format {column name: value types}:

marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
class: >50K, <=50K

Now, I want you to help me identify the problematic functional dependencies from the following functional dependencies, where the functional dependency format is:

Select the non-conforming functional dependencies and return these bad functional dependencies."

Please provide the list of functional dependencies you want me to check, and I'll assist you in identifying the problematic ones.
'''