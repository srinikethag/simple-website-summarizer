from models.llama_loader import LlamaLoader
from models.openai_loader import OpenAiLoader


def get_model(model_type):
    model_classes = {
        "llama": LlamaLoader,
        "openai": OpenAiLoader
    }

    if model_type.lower() in model_classes:
        return model_classes[model_type.lower()]("model_name")

    raise ValueError(f"Unsupported model type: {model_type}")

