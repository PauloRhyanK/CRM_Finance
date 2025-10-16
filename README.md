# CRM FINANCE
## ⚙️ Stack de Tecnologias

Este projeto foi construído utilizando as seguintes tecnologias e bibliotecas principais:

- **Backend:**
  - **Flask:** Um micro-framework web leve e flexível para Python.
  - **Flask-SQLAlchemy:** Extensão que integra o SQLAlchemy para Mapeamento Objeto-Relacional (ORM), facilitando a interação com o banco de dados.
  - **Flask-Migrate:** Extensão para lidar com migrações de esquema do banco de dados utilizando o Alembic.
- **Banco de Dados:**
  - **PostgreSQL:** Um sistema de gerenciamento de banco de dados objeto-relacional poderoso e de código aberto.
  - **Psycopg2:** O driver mais popular para conectar aplicações Python ao PostgreSQL.
- **Ambiente e Configuração:**
  - **Python-dotenv:** Para gerenciar variáveis de ambiente e manter as configurações seguras e separadas do código-fonte.
  - **Docker:** Para containerização da aplicação e do banco de dados, garantindo um ambiente de desenvolvimento e produção consistente.
  
## 📁 Estrutura do Projeto

O projeto utiliza uma arquitetura em camadas, seguindo o padrão *Application Factory* e *Blueprints* para garantir a máxima organização, testabilidade e escalabilidade.

- **`manage.py` / `app.py`**: Pontos de entrada da aplicação.
- **`config.py`**: Define as configurações para os ambientes de desenvolvimento e produção.
- **`app/__init__.py`**: Contém a fábrica `create_app()` que constrói a aplicação, inicializa extensões e regista os blueprints.

- **`app/models/`**: **Camada de Dados**
  - Define a estrutura do banco de dados através de modelos SQLAlchemy. Cada modelo (ex: `customer_model.py`) representa uma tabela.

- **`app/services/`**: **Camada de Lógica de Negócio**
  - Contém a lógica central da aplicação (ex: `customer_service.py`). As funções aqui orquestram as operações, como validar dados e interagir com os modelos para persistir informações no banco.

- **`app/main/routes/`**: **Camada de Apresentação (API)**
  - Define os endpoints da API utilizando Blueprints do Flask. Os ficheiros de rotas (ex: `customer_routes.py`) são responsáveis por receber os pedidos HTTP, chamar a camada de serviço apropriada e retornar a resposta ao cliente.

## ▶️ Como Executar o Projeto

Para executar este projeto em um ambiente de desenvolvimento, é necessário ter o **Docker** e o **Docker Compose** instalados.

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_PROJETO>
    ```

2.  **Crie o ficheiro de ambiente:**
    Copie o ficheiro de exemplo `.env.example` para um novo ficheiro chamado `.env`.
    ```bash
    cp .env.example .env
    ```
    *Revise o ficheiro `.env` e ajuste as variáveis se necessário.*

3.  **Suba os contêineres:**
    Este comando irá construir a imagem da aplicação Flask e iniciar o contêiner do PostgreSQL.
    ```bash
    docker-compose up --build -d
    ```

4.  **Execute as migrações do banco de dados:**
    Com os contêineres em execução, aplique o esquema do banco de dados pela primeira vez.
    ```bash
    docker-compose exec -e FLASK_APP=manage.py backend flask db upgrade
    ```

5.  **Pronto!** A API estará disponível no endereço `http://localhost:5000`.

## 🗃️ Modelos de Dados (Estrutura do Banco)

A base de dados do CRM é composta por três modelos principais que representam as entidades centrais do sistema.

### 1. `User` (Usuário)
- Representa um usuário do sistema (um funcionário da empresa, por exemplo).
- Responsável pela autenticação e pelo registro de quem realizou as transações.
- Campos principais: `id`, `nome`, `email` e `senha` (armazenada com hash seguro).

### 2. `Customer` (Cliente)
- Representa um cliente da empresa. É a entidade central do CRM.
- Armazena todas as informações de contato, endereço e documentos do cliente.
- Campos principais: `id`, `nome`, `email`, `telefone`, `CPF/CNPJ` e `endereço`.
- Possui campos de controle como `data de criação`, `data de atualização` e `status de atividade`.

### 3. `Transaction` (Transação)
- Representa uma transação financeira (entrada ou saída) associada a um usuário.
- *Futuramente, será associada também a um cliente.*
- Campos principais: `id`, `valor`, `tipo de transação` e `data`.


## 🧠 Lógica de Negócio (Camada de Serviço)

A lógica central da aplicação reside na camada de serviço (`app/services/`), que orquestra todas as operações de dados e regras de negócio.

### Autenticação (`auth_service.py`)
- **Registro de Novos Usuários:** Permite o cadastro de novos usuários, garantindo que o email seja único e armazenando a senha de forma segura com hash.
- **Autenticação de Usuários:** Valida as credenciais (email e senha) para permitir o login no sistema.

### Gerenciamento de Clientes (`customer_service.py`)
- **CRUD Completo:** Implementa todas as operações de Criar, Ler, Atualizar e Deletar clientes.
- **Paginação:** A listagem de clientes é paginada para garantir a performance da API, mesmo com um grande volume de dados.
- **Busca Flexível:** Permite a busca de clientes por nome, email ou CPF/CNPJ.
- **Soft Delete:** Ao invés de apagar um cliente permanentemente, o sistema por padrão apenas o marca como "inativo", preservando o histórico de dados. Há também a opção de reativar um cliente.







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