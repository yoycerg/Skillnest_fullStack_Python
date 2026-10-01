# ERD - BookHub

```mermaid
erDiagram
    USERS ||--o{ BOOKS : publica
    GENRES ||--o{ BOOKS : clasifica
    USERS ||--o{ FAVORITES : crea
    BOOKS ||--o{ FAVORITES : recibe

    USERS {
        INT id PK
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR email UK
        VARCHAR password_hash
        TIMESTAMP created_at
    }

    GENRES {
        INT id PK
        VARCHAR name UK
    }

    BOOKS {
        INT id PK
        VARCHAR title
        VARCHAR author
        INT genre_id FK
        DATE publication_date
        TEXT description
        INT user_id FK
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    FAVORITES {
        INT user_id PK, FK
        INT book_id PK, FK
        TIMESTAMP created_at
    }
```

## Relaciones

- Un usuario puede publicar muchos libros.
- Un género puede clasificar muchos libros.
- Un usuario puede marcar muchos libros como favoritos.
- Un libro puede estar en favoritos de muchos usuarios.
- `favorites` resuelve la relación muchos-a-muchos entre usuarios y libros.
