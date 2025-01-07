import requests
import os

# Replace these with your actual values
GITHUB_TOKEN = os.getenv('KOTLIN_TOKEN')
GITHUB_USERNAME = 'pjkundert'
REPO_NAME = 'kotlin-holo'
API_URL = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/issues'

# Define the tasks
tasks = [
    {
        "title": "Initialize Holochain Project",
        "body": "Setup Holochain environment with HDK v0.5.0 and HDI 0.4.0.\nCreate new Holochain DNA for the project."
    },
    {
        "title": "Create Keypair Generation for Basic Users",
        "body": "Implement keypair generation using email and password.\nStore generated agent keypair in Holochain."
    },
    {
        "title": "Designate Recovery Partners",
        "body": "Implement functionality to designate 2+ recovery partners during onboarding.\nEnsure recovery partners create agents using email and password."
    },
    {
        "title": "Implement Simple Authentication API",
        "body": "Develop API endpoints for authentication compatible with Kotlin client apps.\nEnsure API supports login using generated agent keypairs."
    },
    {
        "title": "Associate New Device with Existing Identity",
        "body": "Implement functionality for existing users to associate new devices with their identity.\nEnsure new devices generate an agent keypair and associate with the existing identity."
    },
    {
        "title": "Implement Key Revocation and Recovery",
        "body": "Develop functionality for key revocation using designated recovery partners.\nImplement recovery process using recovery partners' agents.\nSupport key revocation/recovery using external hardware wallets for advanced users."
    },
    {
        "title": "Support External Hardware Wallets",
        "body": "Integrate external hardware wallets for keypair generation.\nEnsure compatibility with key revocation/recovery processes."
    },
    {
        "title": "Develop Javascript Binding for Client Interaction",
        "body": "Create Javascript bindings to interact with Holochain via WebSockets.\nEnsure bindings support keypair generation, authentication, device association, and recovery processes."
    },
    {
        "title": "Testing",
        "body": "Write unit tests for all functionalities.\nConduct integration tests to ensure smooth flow of onboarding, authentication, and recovery processes."
    },
    {
        "title": "Documentation",
        "body": "Document the API endpoints and usage.\nProvide a guide for setting up the system and integrating with client apps.\nWrite user guides for basic and advanced users."
    }
]

# Create issues
for task in tasks:
    response = requests.post(
        API_URL,
        json=task,
        headers={
            'Authorization': f'token {GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }
    )
    if response.status_code == 201:
        print(f'Successfully created issue: {task["title"]}')
    else:
        print(f'Failed to create issue: {task["title"]}, Response: {response.content}')
