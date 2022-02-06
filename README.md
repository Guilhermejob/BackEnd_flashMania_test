## Instalação

- Primeiro faça o fork deste [repositório](https://github.com/Guilhermejob/BackEnd_flashMania_test)

- Em seguida faça um git clone para a sua maquina


- Crie o ambiente um ambiente [virtual em python](https://docs.python.org/pt-br/3/tutorial/venv.html)

```
$ python -m venv venv --upgrade-deps
```


- Entre no ambiente virtual

```
$ source venv/bin/activate
```

- Instale as dependencias no arquivo `requirements.txt`

```
$ pip install -r requirements.txt
```


- Configure suas variáveis segundo o arquivo `.env.example`

- Inicie a aplicação local através do comando

```
$ flask run
```

> #### OBS : todas as requisições de cadastro de dados e atualização são feitos via multipart/form-data

## Requisição de Get all Products

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/152690839-35d9abdf-ca4e-4522-a069-b7f1ff1b57d1.png" width="700px" />
</div>

#

## Requisição de Register new product

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/152691001-680be5db-5e1d-43dc-a8c4-050111245cd7.png" width="700px" />
</div>

#

## Requisição de Patch new product

Se atente em passar o id do produto na rota para conseguir fazer a atualização dos dados

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/152691064-b0baa57e-8531-423d-98e3-f6dc0da9488c.png" width="700px" />
</div>

#

## Requisição de delete product

Se atente em passar o id do produto na rota para conseguir fazer a deleção dos dados

<div align="center">
<img src="https://user-images.githubusercontent.com/80132755/152691173-9c2a31f8-9097-403d-9719-2476fb21dfd2.png" width="700px" />
</div>








