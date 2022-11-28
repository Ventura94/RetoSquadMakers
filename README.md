# Reto SquadMakers

## Tecnologías empleadas:

![image](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white)
![image](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
![image](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![image](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

#### El proyecto requiere de las siguientes variables de entorno:

#### Requerimientos

1. Una base de Datos SQL(Para el desarrollo utilicé Postgres)
2. Instalar los paquetes necesarios:

 ```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

Nota: El segundo archivo es para poder usar los test con pytest y otras herramientas de
desarrollo [coverage, pylint, mypy]

3. Configurar variables de entorno(estas se encuentran dentro de settings.py en la raíz del proyecto):

```python
DATABASE_URL: str  # Base de datos 
TEST_DATABASE_URL: str  # Base de Datos solo para Test
TEST: bool | None  # Hace referencia a si el entorno en el que está corriendo el proyecto es el de test 
```

4. Correr los test:

```bash
pytest
```

5. Correr el proyecto:

```
python -m uvicorn main:app --reload
```

Nota: La url de la documentación: "http://127.0.0.1:8000/docs"

> Se agregó además un GithubAction para correr test en la rama main

## Respuesta a la pregunta 2 del reto:

1. De las opciones a elegir, seleccionaría PostgreSQL, tal como la seleccioné para el desarrollo del presente reto,
   porque es una BD que admite tanto los datos relacionales como no relacionales, es muy madura y probada y además
   maneja
   fácilmente las consultas complejas.
2. La sentencia para crear una base de datos en posgresql seria:

```postgresql
CREATE DATABASE nuevadb WITH OWNER nombreusuario;
```

3. El modelo de datos requerido para este proyecto:

```postgresql
create table joke
(
    id        serial
        primary key,
    create_at timestamp,
    is_delete boolean,
    delete_at timestamp,
    joke      varchar not null
);

alter table joke
    owner to nombreusuario;

create index ix_joke_id
    on joke (id);
```

4. Crear coleccion en MongoDBÑ

```shell
db.createCollection(joke)
```

5. Insertar dentro de la coleccion:

```shell
db.collection.insert()
```

Dentro del insert agregaría un arreglo de documentos 