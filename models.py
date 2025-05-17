from langchain_core.language_models.chat_models import BaseChatModel 
from langchain_ollama import ChatOllama 
from config import Config, ModelConfig, ModelProvider 


def create_llm(model_config: ModelConfig) -> BaseChatModel: 
    if model_config.provider == ModelProvider.OLLAMA: 
        return ChatOllama( 
            model=model_config.name,
            base_url="http://27.147.159.197:11434",
            temperature=model_config.temperature, 
            num_ctx=Config.OLLAMA_CONTEXT_WINDOW, 
            verbose=False, 
            keep_alive=-1, 
        ) 
    elif model_config.provider == ModelProvider.QWEN:
        return ChatOllama(
            model=model_config.name,
             base_url="http://27.147.159.197:11434",
            temperature=model_config.temperature,
            num_ctx=Config.OLLAMA_CONTEXT_WINDOW,
            verbose=False,
            keep_alive=-1,
        )
    else:
        raise ValueError(f"Unsupported model provider: {model_config.provider}")