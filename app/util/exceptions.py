# app/util/exceptions.py

class ServiceError(Exception):
    """Classe base para erros de serviço, permite definir uma mensagem e um status code HTTP."""
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.status_code = status_code

# --- Erros de Autenticação ---
class UserAlreadyExistsError(ServiceError):
    def __init__(self, message="Email já cadastrado."):
        super().__init__(message, status_code=409)  # 409 Conflict

class AuthenticationError(ServiceError):
    def __init__(self, message="Email ou senha inválidos."):
        super().__init__(message, status_code=401)  # 401 Unauthorized

# --- Erros de Cliente ---
class CustomerNotFoundError(ServiceError):
    def __init__(self, message="Cliente não encontrado."):
        super().__init__(message, status_code=404)  # 404 Not Found

class InvalidDataError(ServiceError):
    """Usado para erros de validação de dados de negócio, como CPF inválido."""
    def __init__(self, message, status_code=400):
        super().__init__(message, status_code)