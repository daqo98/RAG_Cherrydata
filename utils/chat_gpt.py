from django.conf import settings
import openai


openai.api_key = settings.OPENAI_API_KEY

CHARTS = ["pie chart","bubble chart", "whiskers", "scatter plot", "box-plot",
        "box and whisker plot", "line graph", "bar chart", "area graph", "histogram", "heatmap"]

class ChatGPTHandler:
    def __init__(self, _user_prompt):
        self.user_prompt = self.remove_extra_spaces(_user_prompt.lower())
        self.chart_type = self.extract_chart_type()

    def remove_extra_spaces(self, input_string):
        return ' '.join(input_string.split())

    def extract_chart_type(self):
        chart_type = next((c for c in CHARTS if c in self.user_prompt), None) # "placeholder"

        return chart_type


    def generate_response(self):
        response = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an helpful assistant."},
                {"role": "user", "content": self.user_prompt},
            ]
        )
        return response.choices[0].message.content.strip()