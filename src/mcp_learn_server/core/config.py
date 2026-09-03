from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MCP_", env_file=".env", extra="ignore", env_file_encoding="utf-8")

    # transport mode for mcp server, "stdio" as default
    transport: str = Field(default="stdio")

    # only relevant when transport is "http"
    http_host: str = Field(default="127.0.0.1")
    http_port: int = Field(default=8080)

    # toggles structured JSON logs (prod) vs readable console logs (dev)
    json_logs: bool = Field(default=True)

settings = Settings()