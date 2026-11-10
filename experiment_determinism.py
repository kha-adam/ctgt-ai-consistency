from llm_client import ask
from statistics import mean

prompt = "Write a one sentence slogan for a coffe shop"

max_tokens=60
n = 10

def attempts(prompt, n = 10, temperature = 0.8, seed = None):
    list_of_texts = []
    latencies = []
    for i in range(n):
        reply = ask(prompt, temperature, seed, max_tokens)
        list_of_texts.append(reply["text"])
        latencies.append(reply["latency_s"])
    mean_latency = mean(latencies)
    unique = len(set(list_of_texts))
    return {
            "texts": list_of_texts,
            "mean_latency": mean_latency,
            "unique": unique,
           }

if __name__ == "__main__":
    
    ask(prompt, max_tokens=max_tokens)
    
    settings = {
            "prompt" : prompt,
            "n" : n,
            "temperature" : 0,
            "seed" : 42,
            }

    A = attempts(**settings)
    print(f"For {settings["temperature"]} and {settings["seed"] if settings["seed"] is not None else "no"} seed, there are {A["unique"]} unique texts\nAverage latency is {A["mean_latency"]}")

    settings["temperature"] = 0.8
    B = attempts(**settings)
    print(f"For {settings["temperature"]} and {settings["seed"] if settings["seed"] is None else "no"} seed, there are {B["unique"]} unique texts\nAverage latency is {B["mean_latency"]}")

    settings["seed"] = None 
    C = attempts(**settings)
    print(f"For {settings["temperature"]} and {settings["seed"] if settings["seed"] is not None else "no"} seed, there are {C["unique"]} unique texts\nAverage latency is {C["mean_latency"]}")   

    print(C["texts"])
