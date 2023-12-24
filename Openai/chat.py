import os
import json
import openai
prompt = '''
"In a database's relational model, there are some columns with continuous values along with their meanings and possible values. There is format 'column name:(maximum value, minimum value, average value, median)':
age:{}
fnlwgt:{}
education-num:{}
capital-gain:{}
capital-loss:{}
hours-per-week:{}

Then,there are columns with enumerable value types in the format 'column name: value types':

marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
class: >50K, <=50K

There are some possible condition function dependencies  behind these columns with enumerable value.For example, when the column “relationship" is husband, then the sex must be “Male”.In addition to the function dependency mentioned above, there may be other possible dependencies here, such as：
'''

prompt_chat_complete = '''
"In a database's relational model, I will provide you with columns with continuous values along with their meanings and possible values. I will provide you with this format 'column name:(maximum value, minimum value, average value, median)':

age:{}
fnlwgt:{}
education-num:{}
capital-gain:{}
capital-loss:{}
hours-per-week:{}

Then, I will give you columns with enumerable value types in the format 'column name: value types':

marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
class: >50K, <=50K

There are some possible condition function dependencies  behind these columns with enumerable value.For example, when the column “relationship" is husband, then the sex must be “Male”. I want you to give me some condition function dependencies like that and orgnize them with form like this:
"1. If the column "relationship" is "Husband", then the column "sex" must be "Male"."
"
'''

prompt_chat_complete_FD = '''
"In a database's relational model, I will provide you with columns with continuous values along with their meanings and possible values. I will provide you with this format 'column name:(maximum value, minimum value, average value, median)':

age:{}
fnlwgt:{}
education-num:{}
capital-gain:{}
capital-loss:{}
hours-per-week:{}

Then, I will give you columns with enumerable value types in the format 'column name: value types':

marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
class: >50K, <=50K

I want you to help me find the possible function dependencies from these columns and return them.
"
'''

prompt_continue = "Can you give some more examples?"

class OpenAIInterface:
    def __init__(self,max_token):
        openai.api_key = os.getenv("AZURE_OPENAI_KEY")
        print("Azure key")
        # print(openai.api_key)
        openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
        openai.api_type = 'azure'
        openai.api_version = '2023-07-01-preview'  # this may change in the future
        self.deployment_name = 'gpt-35-turbo'  # This will correspond to the custom name you chose for your deployment when you deployed a model
        self.max_token = max_token
    def send_completion_job(self, args, prompt_template):
        start_phrase = prompt_template.format(*args)
        # print(start_phrase)
        response = openai.Completion.create(engine=self.deployment_name, prompt=start_phrase, max_tokens=self.max_token)
        text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
        return text

    def send_chat_completion_job(self, args, prompt_template):
        message = prompt_template.format(*args)
        # print(message)
        message_text = [{"role": "system", "content": message}]
        completion = openai.ChatCompletion.create(
            engine="gpt-35-turbo-0613",
            messages=message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        text = completion['choices'][0]['message']['content']
        return text

    def send_chat_completion_job_gpt4(self, args, prompt_template):
        message = prompt_template.format(*args)
        # print(message)
        message_text = [{"role": "user", "content": message}]
        openai.api_base = "https://promptdeltass.openai.azure.com/"
        openai.api_key = "67be85e5dd964d8ab121571a39ed168a"
        # self.deployment_name = "gpt4"
        completion = openai.ChatCompletion.create(
            engine="gpt-4",
            messages=message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        text = completion['choices'][0]['message']['content']
        message_text.append({"role": "assistant", "content": text})
        return text, message_text

    def send_chat_completion_job_gpt4_continue(self, message_text):
        message_text.append({"role": "user", "content": prompt_continue})

        openai.api_base = "https://promptdeltass.openai.azure.com/"
        openai.api_key = "67be85e5dd964d8ab121571a39ed168a"
        completion = openai.ChatCompletion.create(
            engine="gpt-4",
            messages=message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        text = completion['choices'][0]['message']['content']
        print(message)
        message.append({"role": "assistant", "content": text})
        return text, message



    def analysis_data(self, attribute_list):
        def convert_and_analyze(data):
            # 将字符串列表转换为整数列表
            int_list = [int(item) for item in data]

            if not int_list:
                return None  # 空列表时返回 None

            # 计算最大值、最小值、平均值和中位数
            max_value = max(int_list)
            min_value = min(int_list)
            average = sum(int_list) / len(int_list)

            # 中位数计算
            sorted_list = sorted(int_list)
            n = len(sorted_list)
            if n % 2 == 0:
                median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
            else:
                median = sorted_list[n // 2]

            return max_value, min_value, average, median
        analysis = []
        for i in range(len(attribute_list)):
            analysis.append([])
            analysis[i] = convert_and_analyze(attribute_list[i])
        return analysis

if __name__ == "__main__":
    continue_data =[['39', '50', '38', '53', '28', '37', '49', '52', '31', '42'],
     ['77516', '83311', '215646', '234721', '338409', '284582', '160187', '209642', '45781', '159449'],
     ['13', '13', '9', '7', '13', '14', '5', '9', '14', '13'],
     ['2174', '0', '0', '0', '0', '0', '0', '0', '14084', '5178'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
     ['40', '13', '40', '40', '40', '40', '16', '45', '50', '40']]
    message = []
    openai_interface = OpenAIInterface(200)
    #
    print(continue_data)
    analysis = openai_interface.analysis_data(continue_data)
    print("analysis:")
    # print(analysis)
    #
    completion_result, message = openai_interface.send_chat_completion_job_gpt4(analysis,prompt_template=prompt_chat_complete)
    print(completion_result)

    for i in range(1):
        completion_result, message = openai_interface.send_chat_completion_job_gpt4_continue(message)
        print(completion_result)
    # You can call the 'translate_and_identify_dependencies' method with the 'prompt' as needed.
    # result = openai_interface.translate_and_identify_dependencies(prompt)

