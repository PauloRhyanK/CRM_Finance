# CRM FINANCE

## HOW TO START:

### Desenvolvimento Local (Recomendado):

1. **Instalar PostgreSQL:**
```bash
# Windows (usando Chocolatey)
choco install postgresql

# Ou baixar do site oficial: https://www.postgresql.org/download/windows/
# Configurar usuário 'postgres' com senha '1234'
```

2. **Criar banco de dados:**
```bash
# Conectar ao PostgreSQL
psql -U postgres

# Criar banco
CREATE DATABASE crm_db;
\q
```

3. **Instalar dependências Python:**
```bash
pip install -r requirements.txt
```

4. **Inicializar banco de dados:**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. **Executar aplicação:**

**Windows PowerShell (Recomendado):**
```powershell
./init.ps1
```

**Windows Command Prompt:**
```cmd
init.bat
```

**Linux/Unix/WSL:**
```bash
chmod +x init.bash
./init.bash
```

**Ou manualmente:**
```powershell
# PowerShell
$env:FLASK_APP = "app.py"
C:/Programs/Repositorios/Faculdade/CRM_Finance/.venv/Scripts/python.exe app.py

# Ou simplesmente
python app.py
```

### Docker (Produção):

- **Build:**
```bash
docker build -t crm-backend .
```

- **Rodar Container:**
```bash
docker run crm-backend
```

**Docker Compose:**
```bash
# Roda em background (detached)
docker-compose up -d

# Rebuilda as imagens antes de subir
docker-compose up --build

# Para parar tudo
docker-compose down

# Ver logs
docker-compose logs backend
docker-compose logs database

# Entrar no container
docker-compose exec backend bash
```

## Estrutura do Projeto:

```
├── app/
│   ├── __init__.py          # Application Factory
│   ├── main/
│   │   ├── routes/          # Rotas organizadas
│   │   │   ├── auth_routes.py
│   │   │   └── route_manager.py
│   │   └── services/        # Lógica de negócio
│   └── models/              # Modelos do banco de dados
├── config.py                # Configurações
├── app.py                   # Ponto de entrada
├── requirements.txt         # Dependências Python
├── init.ps1                 # Script inicialização Windows PowerShell
├── init.bat                 # Script inicialização Windows CMD
└── init.bash                # Script inicialização Linux/Unix
```

## API Endpoints:

- `GET /` - Página inicial
- `POST /auth/register` - Registro de usuário
- `POST /auth/login` - Login de usuário

### Testando a API:

**Registro de usuário:**
```bash
curl -X POST http://127.0.0.1:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "ds_user": "joao",
    "ds_user_email": "joao@email.com",
    "password": "minhasenha123"
  }'
```

**Login:**
```bash
curl -X POST http://127.0.0.1:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "ds_user_email": "joao@email.com",
    "password": "minhasenha123"
  }'
```

## Ambiente de Desenvolvimento:

- Python 3.11+
- Flask
- SQLAlchemy (SQLite para dev, PostgreSQL para prod)
- Flask-Migrate para migrações

### Hot Reload (Auto-atualização):

✅ **O servidor atualiza automaticamente quando você modificar:**
- Arquivos `.py` (rotas, modelos, serviços)
- Templates HTML
- Arquivos estáticos (CSS, JS)

❌ **Precisa reiniciar manualmente quando modificar:**
- Arquivo `.env` 
- Configurações de banco de dados
- Dependências (`requirements.txt`)

### Configuração de Banco de Dados:

**PostgreSQL (Recomendado - Paridade com Produção):**
- Mesma engine usada em produção
- Recursos avançados (triggers, views, etc.)
- Melhor para testar queries complexas
- Configuração atual no projeto

**Instalação PostgreSQL no Windows:**
1. Baixe em: https://www.postgresql.org/download/windows/
2. Durante instalação, configure:
   - Usuário: `postgres`
   - Senha: `1234`
   - Porta: `5432`
3. Crie o banco: `CREATE DATABASE crm_db;`

**SQLite (Fallback):**
- Se não conseguir instalar PostgreSQL
- Descomente a linha SQLite no `config.py`
- Comente as linhas PostgreSQL

## Scripts de Inicialização:

- **`init.ps1`** - Windows PowerShell (recomendado)
- **`init.bat`** - Windows Command Prompt
- **`init.bash`** - Linux/Unix/WSL

Os scripts automaticamente:
1. Configuram as variáveis de ambiente Flask
2. Ativam o ambiente virtual
3. Executam a aplicação na porta 5000
4. Habilitam hot reload (auto-atualização)

# Gerenciamento de Clientes 

O sistema de gerenciamento de clientes foi implementado com funcionalidades completas de CRUD (Create, Read, Update, Delete), oferecendo uma API REST robusta para gerenciar clientes no sistema CRM Finance.

## 🏗️ Arquitetura Implementada

### 1. **Modelo de Dados (Customer)**
**Arquivo:** `app/models/customer_model.py`

```python
class Customer(db.Model):
    cd_customer = UUID (Primary Key)
    ds_customer_name = String(255) (NOT NULL)
    ds_customer_email = String(255) (UNIQUE, NOT NULL) 
    ds_customer_phone = String(20)
    ds_customer_cpf_cnpj = String(18) (UNIQUE)
    ds_customer_address = String(500)
    ds_customer_city = String(100)
    ds_customer_state = String(2)
    ds_customer_zip_code = String(10)
    ds_customer_country = String(100) (DEFAULT: 'Brasil')
    dt_customer_created_at = DateTime (NOT NULL, DEFAULT: utcnow)
    dt_customer_updated_at = DateTime (ON UPDATE)
    is_customer_active = Boolean (NOT NULL, DEFAULT: True)
```

**Recursos do Modelo:**
- ✅ Validação de CPF/CNPJ
- ✅ Conversão para dicionário (`to_dict()`)
- ✅ Soft delete (desativação em vez de exclusão)
- ✅ Timestamps automáticos

### 2. **Camada de Serviços**
**Arquivo:** `app/services/customer_service.py`

**Funcionalidades Implementadas:**
- ✅ `create_customer(customer_data)` - Criação com validações
- ✅ `get_all_customers(active_only, page, per_page)` - Lista paginada
- ✅ `get_customer_by_id(customer_id)` - Busca por ID
- ✅ `update_customer(customer_id, customer_data)` - Atualização
- ✅ `delete_customer(customer_id, soft_delete)` - Remoção/Desativação
- ✅ `search_customers(search_term, search_fields, active_only)` - Busca
- ✅ `activate_customer(customer_id)` - Reativação

**Características:**
- Tratamento de exceções
- Validações de integridade
- Suporte a soft delete
- Busca em múltiplos campos
- Paginação

### 3. **API REST (Endpoints)**
**Arquivo:** `app/main/routes/customer_routes.py`

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/customers` | Criar cliente |
| `GET` | `/api/customers` | Listar clientes (paginado) |
| `GET` | `/api/customers/{id}` | Buscar cliente por ID |
| `PUT` | `/api/customers/{id}` | Atualizar cliente |
| `DELETE` | `/api/customers/{id}` | Remover/Desativar cliente |
| `PATCH` | `/api/customers/{id}/activate` | Reativar cliente |
| `GET` | `/api/customers/search` | Buscar clientes |

## 📋 Estrutura do Banco de Dados

**Tabela:** `customer`

```sql
CREATE TABLE customer (
    cd_customer UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ds_customer_name VARCHAR(255) NOT NULL,
    ds_customer_email VARCHAR(255) UNIQUE NOT NULL,
    ds_customer_phone VARCHAR(20),
    ds_customer_cpf_cnpj VARCHAR(18) UNIQUE,
    ds_customer_address VARCHAR(500),
    ds_customer_city VARCHAR(100),
    ds_customer_state VARCHAR(2),
    ds_customer_zip_code VARCHAR(10),
    ds_customer_country VARCHAR(100) DEFAULT 'Brasil',
    dt_customer_created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT (now() at time zone 'utc'),
    dt_customer_updated_at TIMESTAMP WITHOUT TIME ZONE,
    is_customer_active BOOLEAN NOT NULL DEFAULT true
);
```

## 🚀 Exemplos de Uso da API

### 1. **Criar Cliente**
```http
POST /api/customers
Content-Type: application/json

{
    "ds_customer_name": "João Silva",
    "ds_customer_email": "joao.silva@email.com",
    "ds_customer_phone": "(11) 99999-9999",
    "ds_customer_cpf_cnpj": "123.456.789-00",
    "ds_customer_address": "Rua das Flores, 123",
    "ds_customer_city": "São Paulo",
    "ds_customer_state": "SP",
    "ds_customer_zip_code": "01234-567"
}
```

**Resposta (201):**
```json
{
    "message": "Cliente criado com sucesso",
    "customer": {
        "cd_customer": "123e4567-e89b-12d3-a456-426614174000",
        "ds_customer_name": "João Silva",
        "ds_customer_email": "joao.silva@email.com",
        "ds_customer_phone": "(11) 99999-9999",
        "ds_customer_cpf_cnpj": "123.456.789-00",
        "ds_customer_address": "Rua das Flores, 123",
        "ds_customer_city": "São Paulo",
        "ds_customer_state": "SP",
        "ds_customer_zip_code": "01234-567",
        "ds_customer_country": "Brasil",
        "dt_customer_created_at": "2025-10-14T15:30:00.000Z",
        "dt_customer_updated_at": null,
        "is_customer_active": true
    }
}
```

### 2. **Listar Clientes (Paginado)**
```http
GET /api/customers?page=1&per_page=20&active_only=true
```

**Resposta (200):**
```json
{
    "customers": [...],
    "total": 50,
    "pages": 3,
    "current_page": 1,
    "per_page": 20
}
```

### 3. **Buscar Cliente por ID**
```http
GET /api/customers/123e4567-e89b-12d3-a456-426614174000
```

### 4. **Atualizar Cliente**
```http
PUT /api/customers/123e4567-e89b-12d3-a456-426614174000
Content-Type: application/json

{
    "ds_customer_name": "João Silva Santos",
    "ds_customer_phone": "(11) 88888-8888"
}
```

### 5. **Buscar Clientes**
```http
GET /api/customers/search?q=João&fields=name,email&active_only=true
```

### 6. **Desativar Cliente (Soft Delete)**
```http
DELETE /api/customers/123e4567-e89b-12d3-a456-426614174000
```

### 7. **Reativar Cliente**
```http
PATCH /api/customers/123e4567-e89b-12d3-a456-426614174000/activate
```

## ✅ Validações Implementadas

1. **Campos Obrigatórios:**
   - Nome do cliente (`ds_customer_name`)
   - Email (`ds_customer_email`)

2. **Unicidade:**
   - Email único no sistema
   - CPF/CNPJ único (quando informado)

3. **Formato:**
   - CPF: 11 dígitos
   - CNPJ: 14 dígitos
   - UUID válido para IDs

4. **Integridade:**
   - Tratamento de violações de chave única
   - Rollback automático em caso de erro

## 🔒 Segurança e Boas Práticas

- ✅ Validação de UUID para IDs
- ✅ Sanitização de parâmetros de entrada
- ✅ Tratamento de exceções
- ✅ Soft delete por padrão
- ✅ Limitação de resultados por página (máx. 100)
- ✅ Handlers de erro específicos

## 🗂️ Arquivos Criados/Modificados

1. **Novo:** `app/models/customer_model.py`
2. **Novo:** `app/services/customer_service.py`  
3. **Novo:** `app/main/routes/customer_routes.py`
4. **Modificado:** `app/models/__init__.py`
5. **Modificado:** `app/main/routes/route_manager.py`
6. **Novo:** `test_customers.py` (script de teste)

## 🎯 Status de Implementação

| Funcionalidade | Status |
|----------------|--------|
| Modelo de Dados | ✅ Completo |
| Serviços CRUD | ✅ Completo |
| API REST | ✅ Completo |
| Validações | ✅ Completo |
| Banco de Dados | ✅ Criado |
| Testes | ✅ Validado |
| Documentação | ✅ Completo |

## 🚧 Próximos Passos Recomendados

1. **Interface Frontend:** Criar formulários para gerenciar clientes
2. **Relatórios:** Implementar relatórios de clientes
3. **Integração:** Conectar clientes com transações financeiras
4. **Auditoria:** Log de alterações nos dados dos clientes
5. **Backup:** Implementar backup/restore de dados de clientes

---

## 🎉 Sistema Completamente Funcional!

O sistema de gerenciamento de clientes está **100% implementado** e pronto para uso, oferecendo:

- **API REST completa** com todas as operações CRUD
- **Validações robustas** de dados
- **Banco de dados estruturado** no PostgreSQL
- **Arquitetura escalável** seguindo boas práticas
- **Documentação completa** para desenvolvimento e uso

O sistema pode ser utilizado imediatamente para gerenciar clientes no CRM Finance! 🚀