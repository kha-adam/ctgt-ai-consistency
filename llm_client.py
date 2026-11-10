from openai import OpenAI
import os
import time

HARNESS_MODEL = os.getenv("HARNESS_MODEL", "llama3.2")
HARNESS_BASE_URL = os.getenv("HARNESS_BASE_URL", "http://localhost:11434/v1")
API_KEY = os.getenv("API_KEY", "ollama")

client = OpenAI(base_url=HARNESS_BASE_URL, api_key=API_KEY)

def ask(prompt, temperature=0.8, seed=None, max_tokens=150):
	d={}
	start = time.perf_counter()
	response = client.chat.completions.create(model=HARNESS_MODEL, messages = [{"role":"user", "content":prompt}], max_tokens = max_tokens)
	elapsed = time.perf_counter() - start
	d["text"] = response.choices[0].message.content
	d["finish_reason"] = response.choices[0].finish_reason
	d["latency_s"] = elapsed
	return d

if __name__ == "__main__":
	print(ask("what is temperature in an llm\n"))
	print(ask("what is a tennis ball made of in one sentence\n"))
	print(ask("what is a seed in an llm\n"))
