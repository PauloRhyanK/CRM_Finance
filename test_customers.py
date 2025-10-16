import requests
import json

BASE_URL = "http://localhost:5000/api/customers"

# Dados de teste para criação de cliente
customer_data = {
    "ds_customer_name": "João Silva", 
    "ds_customer_email": "joao.silva@email.com", 
    "ds_customer_phone": "(11) 99999-9999", 
    "ds_customer_cpf_cnpj": "123.456.789-00", 
    "ds_customer_address": "Rua das Flores, 123", 
    "ds_customer_city": "São Paulo", 
    "ds_customer_state": "SP", 
    "ds_customer_zip_code": "01234-567"
}

def test_create_customer():
    """Teste de criação de cliente"""
    try:
        response = requests.post(BASE_URL, json=customer_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json().get('customer', {}).get('cd_customer')
    except Exception as e:
        print(f"Erro ao criar cliente: {e}")
        return None

def test_get_customers():
    """Teste de listagem de clientes"""
    try:
        response = requests.get(BASE_URL)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Erro ao listar clientes: {e}")

def test_get_customer_by_id(customer_id):
    """Teste de busca de cliente por ID"""
    try:
        response = requests.get(f"{BASE_URL}/{customer_id}")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Erro ao buscar cliente: {e}")

def test_update_customer(customer_id):
    """Teste de atualização de cliente"""
    try:
        update_data = {
            "ds_customer_name": "João Silva Santos",
            "ds_customer_phone": "(11) 88888-8888"
        }
        response = requests.put(f"{BASE_URL}/{customer_id}", json=update_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")

def test_search_customers():
    """Teste de busca de clientes"""
    try:
        response = requests.get(f"{BASE_URL}/search", params={"q": "João"})
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Erro ao buscar clientes: {e}")

if __name__ == "__main__":
    print("=== Testando Sistema de Gerenciamento de Clientes ===\n")
    
    print("1. Criando cliente...")
    customer_id = test_create_customer()
    print()
    
    if customer_id:
        print("2. Listando todos os clientes...")
        test_get_customers()
        print()
        
        print("3. Buscando cliente por ID...")
        test_get_customer_by_id(customer_id)
        print()
        
        print("4. Atualizando cliente...")
        test_update_customer(customer_id)
        print()
        
        print("5. Buscando clientes...")
        test_search_customers()
        print()
        
        print("=== Testes concluídos ===")
    else:
        print("Não foi possível criar o cliente para os demais testes.")