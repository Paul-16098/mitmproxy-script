import json

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
	# Optional: Target a specific domain or path
	# Define the dictionary you want to send as the body
	payload = {"reasoning_effort": "none", "think": False}

	# Convert the dictionary to a JSON string and assign it to the request text
	if flow.request.text is not None:
		flow.request.text = json.dumps({**(json.loads(flow.request.text)), **payload})
	else:
		print("flow.request.text is None")
