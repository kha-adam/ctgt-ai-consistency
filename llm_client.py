from openai import OpenAI
import os
import time

HARNESS_MODEL = os.getenv("HARNESS_MODEL", "llama3.2")
HARNESS_BASE_URL = os.getenv("HARNESS_BASE_URL", "http://localhost:11434/v1")
HARNESS_API_KEY = os.getenv("HARNESS_API_KEY", "ollama")

client = OpenAI(base_url=HARNESS_BASE_URL, api_key=HARNESS_API_KEY)

def ask(prompt, temperature=0.8, seed=None, max_tokens=150):
	d={}
	params = {"model": HARNESS_MODEL,
		"messages": [{"role": "user", "content":prompt}],
		"max_tokens": max_tokens,
		"temperature": temperature}
	if seed is not None:
		params["seed"] = seed
	start = time.perf_counter()
	response = client.chat.completions.create(**params)
	elapsed = time.perf_counter() - start
	d["text"] = response.choices[0].message.content
	d["finish_reason"] = response.choices[0].finish_reason
	d["latency_s"] = elapsed
	return d

if __name__ == "__main__":
	a = ask("write one slogan for a coffe shop", temperature=0, seed=42, max_tokens = 60)
	b = ask("write one slogan for a coffe shop", temperature=0, seed=42, max_tokens = 60)
	print(a["text"] == b["text"])

