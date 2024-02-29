import re

examples = """
spring:
  cloud:
    config:
      uri: ${config_server_url}
      name: application1, application2, application3, application4
"""

regex = r"name\s*:\s*(?P<integrations>.*)"

match = re.search(regex, examples, flags=re.DOTALL)

if match:
  integrations = match.group("integrations")
  print(f"Integrations: {integrations}")
