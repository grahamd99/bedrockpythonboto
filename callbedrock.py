import boto3
import json
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

region = os.getenv("REGION")
profile = os.getenv("AWSPROFILE", region)

print(f"Profile is: {profile}")

# Create a session using a specific AWS profile
session = boto3.session.Session(profile_name=profile)

# Use the session to create clients/resources
client = session.client("bedrock-runtime")

system = [{ "text": "You are a helpful assistant" }]

messages = [
    {"role": "user", "content": [{"text": "Write a short story about dragons"}]},
]

inf_params = {"maxTokens": 300, "topP": 0.1, "temperature": 0.3}

additionalModelRequestFields = {
    "inferenceConfig": {
         "topK": 20
    }
}

model_response = client.converse(
    modelId="amazon.nova-lite-v1:0", 
    messages=messages, 
    system=system, 
    inferenceConfig=inf_params,
    additionalModelRequestFields=additionalModelRequestFields
)

print("\n[Full Response]")
print(json.dumps(model_response, indent=2))

print("\n[Response Content Text]")
print(model_response["output"]["message"]["content"][0]["text"])
