# 🎯 Configuração Insomnia - CRM Finance Clientes

## 📦 **Arquivo de Importação para Insomnia**

### Environment (Ambiente)
```json
{
  "base_url": "http://localhost:5000",
  "customer_id_1": "",
  "customer_id_2": "",
  "customer_id_3": ""
}
```

---

## 🗂️ **Organização de Pastas Recomendada**

```
📁 CRM Finance - Clientes
├── 📁 1. Criar Clientes
│   ├── ✅ Criar Cliente Completo
│   ├── ✅ Criar Cliente Mínimo  
│   ├── ✅ Criar Cliente PJ
│   ├── ❌ Erro - Email Duplicado
│   └── ❌ Erro - Campos Obrigatórios
├── 📁 2. Listar Clientes
│   ├── ✅ Listar Todos
│   ├── ✅ Listar Paginado
│   ├── ✅ Apenas Ativos
│   └── ✅ Todos (Ativos + Inativos)
├── 📁 3. Buscar Cliente
│   ├── ✅ Buscar por ID
│   ├── ❌ ID Inválido
│   └── ❌ Cliente Inexistente
├── 📁 4. Pesquisar Clientes
│   ├── ✅ Buscar por Nome
│   ├── ✅ Buscar por Email
│   ├── ✅ Buscar por CPF/CNPJ
│   └── ✅ Busca Múltiplos Campos
├── 📁 5. Atualizar Cliente
│   ├── ✅ Atualizar Completo
│   ├── ✅ Atualizar Parcial
│   └── ❌ Erro - Email Existente
├── 📁 6. Remover Cliente
│   ├── ✅ Soft Delete
│   └── ✅ Hard Delete
└── 📁 7. Reativar Cliente
    └── ✅ Reativar
```

---

## 🔧 **Requests Configurados para Insomnia**

### 1. 📝 **POST - Criar Cliente Completo**
```
Método: POST
URL: {{ base_url }}/api/customers
Headers:
  Content-Type: application/json

Body (JSON):
{
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
```

### 2. 📝 **POST - Criar Cliente Mínimo**
```
Método: POST
URL: {{ base_url }}/api/customers
Headers:
  Content-Type: application/json

Body (JSON):
{
  "ds_customer_name": "Maria Oliveira",
  "ds_customer_email": "maria.oliveira@email.com"
}
```

### 3. 📝 **POST - Criar Cliente PJ**
```
Método: POST
URL: {{ base_url }}/api/customers
Headers:
  Content-Type: application/json

Body (JSON):
{
  "ds_customer_name": "Tech Solutions LTDA",
  "ds_customer_email": "contato@techsolutions.com",
  "ds_customer_phone": "(11) 3333-4444",
  "ds_customer_cpf_cnpj": "12.345.678/0001-90",
  "ds_customer_address": "Av. Paulista, 1000",
  "ds_customer_city": "São Paulo",
  "ds_customer_state": "SP",
  "ds_customer_zip_code": "01310-100"
}
```

### 4. 📋 **GET - Listar Todos os Clientes**
```
Método: GET
URL: {{ base_url }}/api/customers
```

### 5. 📋 **GET - Listar com Paginação**
```
Método: GET
URL: {{ base_url }}/api/customers
Query Params:
  page: 1
  per_page: 10
  active_only: true
```

### 6. 🔍 **GET - Buscar Cliente por ID**
```
Método: GET
URL: {{ base_url }}/api/customers/{{ customer_id_1 }}
```

### 7. 🔎 **GET - Pesquisar por Nome**
```
Método: GET
URL: {{ base_url }}/api/customers/search
Query Params:
  q: João
  fields: name
  active_only: true
```

### 8. 🔎 **GET - Pesquisar por Email**
```
Método: GET
URL: {{ base_url }}/api/customers/search
Query Params:
  q: silva
  fields: email
```

### 9. 🔎 **GET - Pesquisar Múltiplos Campos**
```
Método: GET
URL: {{ base_url }}/api/customers/search
Query Params:
  q: Tech
  fields: name,email,cpf_cnpj
  active_only: true
```

### 10. ✏️ **PUT - Atualizar Cliente**
```
Método: PUT
URL: {{ base_url }}/api/customers/{{ customer_id_1 }}
Headers:
  Content-Type: application/json

Body (JSON):
{
  "ds_customer_name": "João Silva Santos Junior",
  "ds_customer_email": "joao.santos@newemail.com",
  "ds_customer_phone": "(11) 88888-8888",
  "ds_customer_address": "Rua Nova, 456",
  "ds_customer_city": "Rio de Janeiro",
  "ds_customer_state": "RJ",
  "ds_customer_zip_code": "20000-000"
}
```

### 11. ✏️ **PUT - Atualizar Parcialmente**
```
Método: PUT
URL: {{ base_url }}/api/customers/{{ customer_id_2 }}
Headers:
  Content-Type: application/json

Body (JSON):
{
  "ds_customer_phone": "(11) 77777-7777"
}
```

### 12. 🗑️ **DELETE - Soft Delete**
```
Método: DELETE
URL: {{ base_url }}/api/customers/{{ customer_id_3 }}
```

### 13. 🗑️ **DELETE - Hard Delete**
```
Método: DELETE
URL: {{ base_url }}/api/customers/{{ customer_id_3 }}
Query Params:
  hard_delete: true
```

### 14. 🔄 **PATCH - Reativar Cliente**
```
Método: PATCH
URL: {{ base_url }}/api/customers/{{ customer_id_3 }}/activate
```

---

## 🧪 **Testes de Erro**

### ❌ **POST - Email Duplicado**
```
Método: POST
URL: {{ base_url }}/api/customers
Headers:
  Content-Type: application/json

Body (JSON):
{
  "ds_customer_name": "Cliente Duplicado",
  "ds_customer_email": "joao.silva@email.com"
}

Esperado: 400 - Email já está em uso
```

### ❌ **POST - Campos Obrigatórios**
```
Método: POST
URL: {{ base_url }}/api/customers
Headers:
  Content-Type: application/json

Body (JSON):
{
  "ds_customer_phone": "(11) 99999-9999"
}

Esperado: 400 - Campo obrigatório ausente
```

### ❌ **GET - ID Inválido**
```
Método: GET
URL: {{ base_url }}/api/customers/invalid-uuid

Esperado: 400 - ID de cliente inválido
```

### ❌ **GET - Cliente Inexistente**
```
Método: GET
URL: {{ base_url }}/api/customers/00000000-0000-0000-0000-000000000000

Esperado: 404 - Cliente não encontrado
```

---

## 📋 **Checklist de Testes**

- [ ] ✅ Criar cliente com dados completos
- [ ] ✅ Criar cliente com dados mínimos
- [ ] ✅ Criar cliente pessoa jurídica
- [ ] ❌ Tentar criar com email duplicado
- [ ] ❌ Tentar criar sem campos obrigatórios
- [ ] ✅ Listar todos os clientes
- [ ] ✅ Listar com paginação
- [ ] ✅ Buscar cliente por ID válido
- [ ] ❌ Buscar cliente com ID inválido
- [ ] ❌ Buscar cliente inexistente
- [ ] ✅ Pesquisar por nome
- [ ] ✅ Pesquisar por email
- [ ] ✅ Pesquisar por CPF/CNPJ
- [ ] ✅ Atualizar dados do cliente
- [ ] ✅ Atualização parcial
- [ ] ❌ Tentar atualizar com email existente
- [ ] ✅ Desativar cliente (soft delete)
- [ ] ✅ Reativar cliente
- [ ] ✅ Remover permanentemente (hard delete)

---

## 🎯 **Respostas Esperadas**

### ✅ **Sucesso:**
- **201 Created**: Cliente criado com sucesso
- **200 OK**: Operação realizada com sucesso
- **200 OK**: Lista ou busca retornada

### ❌ **Erros:**
- **400 Bad Request**: Dados inválidos ou ausentes
- **404 Not Found**: Cliente não encontrado
- **405 Method Not Allowed**: Método HTTP não permitido
- **500 Internal Server Error**: Erro interno do servidor

---

## 💡 **Dicas de Uso:**

1. **Execute os 3 primeiros POSTs** para criar clientes de teste
2. **Copie os IDs** retornados e cole nas variáveis de ambiente
3. **Execute os testes** na ordem sugerida
4. **Observe os códigos** de resposta HTTP
5. **Verifique o banco** ocasionalmente para confirmar as operações


----

# 🚀 Coleção de Testes - Sistema de Clientes CRM Finance

## 📋 Configuração Base
- **Base URL:** `http://localhost:5000`
- **Content-Type:** `application/json`

---

## 1. 📝 **CRIAR CLIENTE**

### ✅ Criar Cliente Completo
```bash
curl -X POST http://localhost:5000/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_name": "João Silva Santos",
    "ds_customer_email": "joao.silva@email.com",
    "ds_customer_phone": "(11) 99999-9999",
    "ds_customer_cpf_cnpj": "123.456.789-00",
    "ds_customer_address": "Rua das Flores, 123, Apt 45",
    "ds_customer_city": "São Paulo",
    "ds_customer_state": "SP",
    "ds_customer_zip_code": "01234-567",
    "ds_customer_country": "Brasil"
  }'
```

### ✅ Criar Cliente Mínimo (Apenas Obrigatórios)
```bash
curl -X POST http://localhost:5000/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_name": "Maria Oliveira",
    "ds_customer_email": "maria.oliveira@email.com"
  }'
```

### ✅ Criar Cliente Pessoa Jurídica
```bash
curl -X POST http://localhost:5000/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_name": "Tech Solutions LTDA",
    "ds_customer_email": "contato@techsolutions.com",
    "ds_customer_phone": "(11) 3333-4444",
    "ds_customer_cpf_cnpj": "12.345.678/0001-90",
    "ds_customer_address": "Av. Paulista, 1000",
    "ds_customer_city": "São Paulo",
    "ds_customer_state": "SP",
    "ds_customer_zip_code": "01310-100"
  }'
```

### ❌ Teste de Erro - Email Duplicado
```bash
curl -X POST http://localhost:5000/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_name": "Cliente Duplicado",
    "ds_customer_email": "joao.silva@email.com"
  }'
```

### ❌ Teste de Erro - Campos Obrigatórios
```bash
curl -X POST http://localhost:5000/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_phone": "(11) 99999-9999"
  }'
```

---

## 2. 📋 **LISTAR CLIENTES**

### ✅ Listar Todos os Clientes (Primeira Página)
```bash
curl -X GET http://localhost:5000/api/customers
```

### ✅ Listar com Paginação
```bash
curl -X GET "http://localhost:5000/api/customers?page=1&per_page=10"
```

### ✅ Listar Apenas Clientes Ativos
```bash
curl -X GET "http://localhost:5000/api/customers?active_only=true"
```

### ✅ Listar Todos (Ativos e Inativos)
```bash
curl -X GET "http://localhost:5000/api/customers?active_only=false"
```

### ✅ Listar com Paginação Customizada
```bash
curl -X GET "http://localhost:5000/api/customers?page=2&per_page=5&active_only=true"
```

---

## 3. 🔍 **BUSCAR CLIENTE ESPECÍFICO**

### ✅ Buscar Cliente por ID
```bash
# Substitua {customer_id} pelo ID real do cliente
curl -X GET http://localhost:5000/api/customers/{customer_id}
```

### ❌ Teste de Erro - ID Inválido
```bash
curl -X GET http://localhost:5000/api/customers/invalid-uuid
```

### ❌ Teste de Erro - Cliente Inexistente
```bash
curl -X GET http://localhost:5000/api/customers/00000000-0000-0000-0000-000000000000
```

---

## 4. 🔎 **BUSCAR CLIENTES (SEARCH)**

### ✅ Buscar por Nome
```bash
curl -X GET "http://localhost:5000/api/customers/search?q=João&fields=name"
```

### ✅ Buscar por Email
```bash
curl -X GET "http://localhost:5000/api/customers/search?q=silva&fields=email"
```

### ✅ Buscar por CPF/CNPJ
```bash
curl -X GET "http://localhost:5000/api/customers/search?q=123.456&fields=cpf_cnpj"
```

### ✅ Buscar em Múltiplos Campos
```bash
curl -X GET "http://localhost:5000/api/customers/search?q=Tech&fields=name,email,cpf_cnpj"
```

### ✅ Buscar Incluindo Inativos
```bash
curl -X GET "http://localhost:5000/api/customers/search?q=Silva&active_only=false"
```

### ✅ Busca Rápida (Endpoint Alternativo)
```bash
curl -X GET "http://localhost:5000/api/customers?search=João"
```

---

## 5. ✏️ **ATUALIZAR CLIENTE**

### ✅ Atualizar Dados Completos
```bash
# Substitua {customer_id} pelo ID real do cliente
curl -X PUT http://localhost:5000/api/customers/{customer_id} \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_name": "João Silva Santos Junior",
    "ds_customer_email": "joao.santos@newemail.com",
    "ds_customer_phone": "(11) 88888-8888",
    "ds_customer_address": "Rua Nova, 456",
    "ds_customer_city": "Rio de Janeiro",
    "ds_customer_state": "RJ",
    "ds_customer_zip_code": "20000-000"
  }'
```

### ✅ Atualizar Apenas Nome
```bash
curl -X PUT http://localhost:5000/api/customers/{customer_id} \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_name": "João Silva (Atualizado)"
  }'
```

### ✅ Atualizar Apenas Telefone
```bash
curl -X PUT http://localhost:5000/api/customers/{customer_id} \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_phone": "(11) 77777-7777"
  }'
```

### ❌ Teste de Erro - Email Já Existente
```bash
curl -X PUT http://localhost:5000/api/customers/{customer_id} \
  -H "Content-Type: application/json" \
  -d '{
    "ds_customer_email": "maria.oliveira@email.com"
  }'
```

---

## 6. 🗑️ **DESATIVAR CLIENTE (SOFT DELETE)**

### ✅ Desativar Cliente (Soft Delete)
```bash
curl -X DELETE http://localhost:5000/api/customers/{customer_id}
```

### ✅ Remover Cliente Permanentemente (Hard Delete)
```bash
curl -X DELETE "http://localhost:5000/api/customers/{customer_id}?hard_delete=true"
```

---

## 7. 🔄 **REATIVAR CLIENTE**

### ✅ Reativar Cliente Desativado
```bash
curl -X PATCH http://localhost:5000/api/customers/{customer_id}/activate
```

---

## 8. 🧪 **TESTES DE VALIDAÇÃO E ERRO**

### ❌ Criar Cliente sem Content-Type
```bash
curl -X POST http://localhost:5000/api/customers \
  -d '{
    "ds_customer_name": "Teste",
    "ds_customer_email": "teste@test.com"
  }'
```

### ❌ Buscar com Termo Vazio
```bash
curl -X GET "http://localhost:5000/api/customers/search?q="
```

### ❌ Página Inválida
```bash
curl -X GET "http://localhost:5000/api/customers?page=-1"
```

### ❌ Método Não Permitido
```bash
curl -X PATCH http://localhost:5000/api/customers
```

---

## 🎯 **SEQUÊNCIA DE TESTE COMPLETA**

Execute na ordem para testar todo o fluxo:

1. **Criar 3 clientes** (usar os 3 primeiros CURLs de criação)
2. **Listar todos** para ver os clientes criados
3. **Buscar específico** usando um ID retornado
4. **Fazer busca** por nome/email
5. **Atualizar um cliente**
6. **Desativar um cliente**
7. **Listar apenas ativos** para confirmar desativação
8. **Reativar o cliente**
9. **Confirmar reativação**

---

## 📊 **VALIDAÇÕES ESPERADAS**

### ✅ **Respostas de Sucesso:**
- **201**: Cliente criado
- **200**: Operação bem-sucedida
- **200**: Lista/busca retornada

### ❌ **Respostas de Erro:**
- **400**: Dados inválidos/ausentes
- **404**: Cliente não encontrado
- **405**: Método não permitido
- **500**: Erro interno do servidor

---

## 🔧 **Dicas para Insomnia:**

1. **Crie um Environment** com:
   ```json
   {
     "base_url": "http://localhost:5000",
     "customer_id": "cole-aqui-um-id-real"
   }
   ```

2. **Use {{ base_url }} e {{ customer_id }}** nos requests

3. **Organize em pastas:**
   - 📁 Criar Clientes
   - 📁 Listar Clientes  
   - 📁 Buscar Clientes
   - 📁 Atualizar Clientes
   - 📁 Remover Clientes
   - 📁 Testes de Erro

4. **Salve IDs** dos clientes criados para usar nos testes de atualização/remoção