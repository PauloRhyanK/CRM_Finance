# CRM FINANCE

## HOW TO START:

Docker:

- Build:
```bash
    docker build -t crm-backend
```
- Rodar Container:
```bash
    docker run crm-backend
```

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