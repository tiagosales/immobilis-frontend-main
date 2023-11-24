# immobilis-frontend-main
Projeto integrado da pós graduação de Desenv. Web Full Stack da PUC Minas
- Para iniciar a aplicação
  1. Crie o arquivo immobilis/immobilis/.env com a variável URL_BACKEND apontando para o endereço da API iniciada no repositorio immobilis-backend-main.
     echo "URL_BACKEND=https://meu.endereco.de.backend:porta" > immobilis/immobilis/.env
  3. Crie um virtualenv com o comando:
     $ python3 -m venv "nomeDoVenv"
  4. Execute o comando de activate respectivo do sistema operacional.
     Ex: Linux:
       $ . ./venv/bin/activate
  6. Instale os pacotes requeridos:
     (venv)$ pip install -r requirements.txt
  7. Iniciar o Django:
     (venv)$ python3 manage.py runserver
