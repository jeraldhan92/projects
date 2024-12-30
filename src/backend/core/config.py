from starlette.config import Config

APP_VERSION = "0.0.1"
APP_NAME = "LawBot"

config = Config(".env") 

# Fastapi 
API_PORT: int = config("API_PORT", cast=int, default=8080)
DEFAULT_CONFIG_PATH: str = config("BACKEND_CONFIG_PATH")

# Langchain
CHAIN_KEY: str = config('CHAIN_KEY')
CHAIN_VERSION: str = config('CHAIN_VERSION')