# -*- coding: utf-8 -*-
"""
Teste da API de Clientes com UTF-8
"""

import requests
import json
import sys

def test_api():
    """Testa a API de clientes"""
    
    base_url = "http://localhost:5000/api"
    
    # Configuração para UTF-8
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json; charset=utf-8'
    }
    
    print("🧪 Testando API de Clientes com UTF-8")
    print("=" * 50)
    
    try:
        # 1. Teste simples de conexão
        print("1. Testando conexão...")
        response = requests.get(f"{base_url}/test", headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✅ Conexão OK")
            print(f"   Resposta: {response.text}")
        else:
            print(f"❌ Erro na conexão: {response.status_code}")
            return
        
        # 2. Teste de criação de cliente
        print("\n2. Testando criação de cliente...")
        
        customer_data = {
            "ds_customer_name": "João Silva Santos",
            "ds_customer_email": "joao.silva@email.com",
            "ds_customer_phone": "(11) 99999-9999",
            "ds_customer_cpf_cnpj": "123.456.789-00",
            "ds_customer_address": "Rua das Flores, 123, Apt 45",
            "ds_customer_city": "São Paulo",
            "ds_customer_state": "SP",
            "ds_customer_zip_code": "01234-567",
            "ds_customer_country": "Brasil"
        }
        
        response = requests.post(
            f"{base_url}/customers",
            headers=headers,
            data=json.dumps(customer_data, ensure_ascii=False).encode('utf-8'),
            timeout=10
        )
        
        if response.status_code == 201:
            print("✅ Cliente criado com sucesso")
            print(f"   Resposta: {response.text}")
            
            # Pega o ID do cliente criado para próximos testes
            customer_id = response.json()['customer']['id_customer']
            
            # 3. Teste de listagem
            print("\n3. Testando listagem de clientes...")
            response = requests.get(f"{base_url}/customers", headers=headers, timeout=10)
            
            if response.status_code == 200:
                print("✅ Listagem OK")
                customers = response.json()['customers']
                print(f"   Total de clientes: {len(customers)}")
                
                # 4. Teste de busca por ID
                print(f"\n4. Testando busca por ID: {customer_id}")
                response = requests.get(f"{base_url}/customers/{customer_id}", headers=headers, timeout=10)
                
                if response.status_code == 200:
                    print("✅ Busca por ID OK")
                    customer = response.json()
                    print(f"   Cliente: {customer['ds_customer_name']}")
                    print(f"   Email: {customer['ds_customer_email']}")
                    print(f"   Cidade: {customer['ds_customer_city']}")
                else:
                    print(f"❌ Erro na busca por ID: {response.status_code}")
                    print(f"   Resposta: {response.text}")
            else:
                print(f"❌ Erro na listagem: {response.status_code}")
                print(f"   Resposta: {response.text}")
        else:
            print(f"❌ Erro na criação: {response.status_code}")
            print(f"   Resposta: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar ao servidor")
        print("   Verifique se o servidor Flask está rodando em http://localhost:5000")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    test_api()