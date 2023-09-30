import os
import openai
from config import apiKey

openai.api_key = apiKey
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to boss for resignation",
  temperature=1,
  max_tokens=347,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
{
  "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
  "id": "cmpl-840RrdJdxTXG6rWrcUxswOZunqNcI",
  "object": "text_completion",
  "created": 1695965727,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nSubject Line: Resignation Notice\n\nDear [Boss Name],\n\nI am writing to inform you of my decision to resign from my position as [Position Title] at [Company Name]. My resignation is effective as of [date].\n\nThis was not an easy decision, but I believe it is the right one for me. I am grateful for the guidance and experience my time with the company has provided.\n\nI have thoroughly enjoyed my role and am proud of the work I have accomplished in the time I have been here. I have appreciated the opportunity to work alongside such talented and driven people and am thankful for your support and mentorship throughout my tenure.\n\nI am more than happy to help during the transition period and will do my best to wrap up any projects I am involved in before my departure.\n\nAgain, thank you for the opportunity to work at [Company Name].\n\nSincerely,\n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 7,
    "completion_tokens": 196,
    "total_tokens": 203
  }
}
'''
