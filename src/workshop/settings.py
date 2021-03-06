from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    port: int = 5000
    database_url: str = 'sqlite:///./sql_app.sqlite3'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
