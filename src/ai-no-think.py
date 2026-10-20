import json

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
	# Optional: Target a specific domain or path
	# Define the dictionary you want to send as the body
	payload = {"reasoning_effort": "none", "think": False}

	# Convert the dictionary to a JSON string and assign it to the request text
	flow.request.text = json.dumps({**(json.loads(flow.request.text)), **payload})

	# Ensure the Content-Type header reflects that you are sending JSON
	# flow.request.headers["Content-Type"] = "application/json"
