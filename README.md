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


## 🚀 Endpoints da API

A API é dividida em dois blueprints principais: Autenticação e Clientes.

### Autenticação (`/auth`)

| Método | Rota             | Descrição                                 | Corpo (JSON)                                       | Resposta de Sucesso (201)                            |
| :----- | :--------------- | :---------------------------------------- | :------------------------------------------------- | :-------------------------------------------------- |
| `POST` | `/register`      | Registra um novo usuário no sistema.      | `{ "ds_user": "Nome", "ds_user_email": "...", "password": "..." }` | `{ "message": "Usuário registrado com sucesso!" }`    |
| `POST` | `/login`         | Autentica um usuário e retorna um token.  | `{ "ds_user_email": "...", "password": "..." }`       | `{ "message": "Login bem-sucedido.", "token": "..." }` |

### Clientes (`/api/customers`)

| Método | Rota                      | Descrição                                         | Corpo/Parâmetros                                                              | Resposta de Sucesso (200/201)                                 |
| :----- | :------------------------ | :------------------------------------------------ | :---------------------------------------------------------------------------- | :---------------------------------------------------------- |
| `POST` | `/`                       | Cria um novo cliente.                             | **Corpo (JSON):** Dados completos do cliente.                               | `{ "message": "Cliente criado...", "customer": {...} }`     |
| `GET`  | `/`                       | Lista todos os clientes com paginação.            | **Query:** `page`, `per_page`, `active_only`                                  | `{ "customers": [...], "total": ..., "pages": ... }`        |
| `GET`  | `/search`                 | Busca clientes por um termo.                      | **Query:** `q` (termo), `fields` (campos), `active_only`                      | `{ "customers": [...], "total": ... }`                       |
| `GET`  | `/<customer_id>`          | Obtém os detalhes de um cliente específico.       | -                                                                             | `{ "customer": {...} }`                                      |
| `PUT`  | `/<customer_id>`          | Atualiza os dados de um cliente.                  | **Corpo (JSON):** Dados parciais ou completos do cliente.                   | `{ "message": "Cliente atualizado...", "customer": {...} }` |
| `DELETE` | `/<customer_id>`        | Desativa (soft delete) ou remove um cliente.      | **Query:** `hard_delete=true` (opcional)                                      | `{ "message": "Cliente desativado/removido..." }`           |
| `PATCH`  | `/<customer_id>/activate` | Reativa um cliente que foi desativado.            | -                                                                             | `{ "message": "Cliente reativado..." }`                     |

### Produtos (`/api/products`)

| Método | Rota             | Descrição                                         | Corpo/Parâmetros                                     | Resposta de Sucesso (200/201)                               |
| :----- | :--------------- | :------------------------------------------------ | :--------------------------------------------------- | :-------------------------------------------------------- |
| `POST` | `/`              | Cria um novo produto ou serviço.                  | **Corpo (JSON):** Dados completos do produto.        | `{ "message": "Produto criado...", "product": {...} }`    |
| `GET`  | `/`              | Lista todos os produtos com paginação.            | **Query:** `page`, `per_page`                        | `{ "products": [...], "total": ..., "pages": ... }`       |
| `GET`  | `/<product_id>`  | Obtém os detalhes de um produto específico.       | -                                                    | `{ "product": {...} }`                                    |
| `PUT`  | `/<product_id>`  | Atualiza os dados de um produto.                  | **Corpo (JSON):** Dados parciais ou completos.       | `{ "message": "Produto atualizado...", "product": {...} }` |
| `DELETE`| `/<product_id>` | Desativa (soft delete) ou remove um produto.      | **Query:** `hard_delete=true` (opcional)             | `{ "message": "Produto desativado/removido..." }`         |