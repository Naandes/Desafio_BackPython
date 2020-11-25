# Desafio

## Api de notícias

### **Overview**

Api para cadastro de notícias, colocando o título, o campo da notícia e o autor. É possível também alterar os dados, fazer busca deletar a notícia caso queira.

### **Technologies**

- Flask
- MongoDb
- Venv

### **Quick start**

- Clonar Repositorio: `git clone https://github.com/Naandes/Desafio_BackPython.git`
- Instalar Python : `https://python.org.br/instalacao-windows/` 
- Instalar Virtualenv: `pip install virtualenv --user`
- Acessar pasta Scripts através do terminal: `cd .\Desafio_BackPython\meuvenv\Scripts`
- Iniciar o Virtualenv no terminal: `activate`
- Acessar pasta src através do terminal: `cd .\Desafio_BackPython\src`
- Iniciar a aplicação: `python app.py`


### **Endpoints**

### Cadastrar regras de horário para atendimento

http://localhost:5000/add **POST**

**Dados Válidos**

Os dados válidos são através da seguinte forma:
```json

  "titulo" : "titulo que deseja para sua notícia",
  "noticia" : "Campo de texto que deseja para sua notícia",
  "autor" : "Autor da sua notícia"

```

**Dados de Retorno**

"Notícia adicionada com sucesso"



### **Busca da notícia**

http://localhost:5000/busca **GET**

**Dados Válidos**

```javascript
  busca: "Palavra a ser buscada";
```

**Dados de Retorno**

```json
[
  {
    "_id": {"$oid": "5fbe86dd00ce1690bd75f871"}, 
    "noticia": "Rainha", 
    "titulo": "Camilla", 
    "autor": "Deus"
  }
]
```

**Obs**

Caso não encontre nada na busca, o vetor retona o vetor vazio

### **Busca da notícia**

http://localhost:5000/delete/<id> **DELETE**

**Dados Válidos**

Somente acessar com o ID da notícia e com a url acima deleta a notícia.

**Dados de Retorno**

"Notícia deletada com sucesso"

### **Busca da notícia**

http://localhost:5000/update/<id> **PUT**  

**Dados Válidos**

Os dados válidos são através da seguinte forma:
```json

  "titulo" : "Modificação do titulo, caso exista",
  "noticia" : "Modificação do campo da notícia, caso exista",
  "autor" : "Modificação do autor, caso exista"

```

**Dados de Retorno**

"Notícia alterada com sucesso"
