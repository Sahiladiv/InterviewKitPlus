from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_explanation(question: str) -> str:
    print("HF Token loaded:", bool(os.getenv("HUGGINGFACEHUB_API_TOKEN")))
    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    print(hf_token)
    # client = InferenceClient(
    #     "deepseek-ai/deepseek-coder-6.7b-instruct",
    #     token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    # )
    client = InferenceClient("bigscience/bloom", token=hf_token)

    response = client.text_generation(
        prompt="What is a binary tree?",
        max_new_tokens=100
    )
    prompt = f"""You are an expert software tutor. Given a coding problem or concept, explain it clearly and concisely.

Question: {question}

Explanation:"""

    response = client.text_generation(
        prompt=prompt,
        max_new_tokens=512,
        temperature=0.7,
        do_sample=True,
    )

    return response.strip()


# {
#   "question": "Explain the difference between BFS and DFS"
# }



