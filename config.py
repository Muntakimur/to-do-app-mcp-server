from dataclasses import dataclass 
from enum import Enum 

class ModelProvider (str, Enum): 
    OLLAMA = "ollama"
    QWEN = "qwen3"
    GROQ = "groq" 

@dataclass 
class ModelConfig: 
    name: str 
    temperature: float 
    provider: ModelProvider 

QWEN = ModelConfig("qwen3", temperature = 0.0, provider=ModelProvider.OLLAMA) 
LLAMA_3_2 = ModelConfig("llama3.2:3b", temperature = 0.0, provider=ModelProvider.OLLAMA) 

class Config: 
    SEED = 42 
    MODEL=QWEN
    OLLAMA_CONTEXT_WINDOW = 4096 # increase to allow longer conversations but slower response 
    class Server: 
        HOST = "0.0.0.0" 
        PORT = 8001 
        SSE_PATH = "/sse" 
        TRANSPORT = "sse" 
    class Agent:
        MAX_ITERATIONS = 5  