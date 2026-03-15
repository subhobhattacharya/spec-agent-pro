import os
from openai import OpenAI

class PRDAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_prd(self, concept):
        print(f"🚀 Architecting spec for: {concept}...")
        
        prompt = f"""
        Act as a Senior Technical Product Manager with 10+ years of experience in Fintech and AI.
        Create a comprehensive PRD in Markdown for the following concept: {concept}
        
        Include these specific sections:
        1. Executive Summary & North Star Metric
        2. User Stories (Gherkin Style: Given/When/Then)
        3. Technical Constraints & API Requirements
        4. Non-Functional Requirements (Security, Scalability, Compliance)
        5. Edge Cases (The 'Corner' cases most PMs miss)
        """

        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# Usage Example
if __name__ == "__main__":
    # In a real scenario, use environment variables for keys
    # agent = PRDAgent(api_key="your-api-key-here")
    # spec = agent.generate_prd("A serverless payment gateway for high-volume aviation transactions")
    # print(spec)
    print("Agent initialized. Ready to generate specs.")
