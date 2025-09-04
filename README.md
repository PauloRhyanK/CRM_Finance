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