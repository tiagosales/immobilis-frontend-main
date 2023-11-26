# immobilis-frontend-main
Projeto integrado da pós graduação de Desenv. Web Full Stack da PUC Minas<br>
- Para iniciar a aplicação<br>
  1. Crie o arquivo immobilis/immobilis/.env com a variável URL_BACKEND apontando para o endereço da API iniciada no repositorio immobilis-backend-main.<br>
     echo "URL_BACKEND=https://meu.endereco.de.backend:porta" > immobilis/immobilis/.env<br>
  3. Crie um virtualenv com o comando:<br>
     $ python3 -m venv "nomeDoVenv"<br>
  4. Execute o comando de activate respectivo do sistema operacional.<br>
     Ex: Linux:<br>
       $ . ./venv/bin/activate<br>
  6. Instale os pacotes requeridos:<br>
     (venv)$ pip install -r requirements.txt<br>
  7. Iniciar o Django:<br>
     (venv)$ cd immobilis; python3 manage.py runserver<br>
