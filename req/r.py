import requests

API_TOKEN = ("017c25cb-c2fe-43ef-b58e-e49320ff407e"
             "")
data = {"login" : "+79776964151"}

response = requests.post("https://id.vk.com/auth?action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInRva2VuIjoiRWhmX184R3FLd3d0Rjd6MDQxU0h0UDdUakVEZGhDWXMyVGZ4R2doSnNiQVRBeThrV3ZTbXRBdG1aVDU0NHFpYnE5c3J1cjdSUjlxZnNiY2VGNlQ0Tk9hNDNZM1A4MUwwNXhlZldlc0tIbkdOY2M5RFp6cWFob1hST1BHSDhyZmdaTzYtVGk4YXBrYmdBcHQwWWh3dkROU2dfckg1dE5oRHlmOXU0Ulo4YTQ4c1BlQUQ1aWMtS0h3WG1ad1ZKY2w5cUptazhhdGpjejZMWUxIc2VrOGFWaHhHemZyMXphaGR3cnpjbE5jaWdJOTRidWJtN1U2S2Y4NWRIRWxaNUNramVaYUtyUS1xY0lSUmhDcEE5X1M5cGciLCJpbnB1dF90eXBlIjoicGhvbmUiLCJwYXJhbXMiOnsidHlwZSI6InNpZ25faW4iLCJjc3JmX2hhc2giOiJiNGE1NGQ4YmUxM2IwODdhY2QifX0%3D&scheme=dark&is_redesigned=1&uuid=mcdfjr&response_type=silent_token&v=1.3.0&app_id=7913379&redirect_uri=https%3A%2F%2Fvk.com%2Fjoin", data=data)
print(response.status_code)