from django.conf import settings
import openai


openai.api_key = settings.OPENAI_API_KEY


class ChatGPTHandler:
    def __init__(self, _user_prompt):
        self.user_prompt = _user_prompt
        self.chart_type = self.parse()


    def parse(self):
        charts = ["pie chart","bubble chart", "whiskers", "scatter", "box-plot",
        "box and whisker plot", "line graph", "bar chart", "area graph", "histogram", "heatmap"]

        chart_type = "placeholder"

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