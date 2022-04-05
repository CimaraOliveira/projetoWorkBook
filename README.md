# Sistema WorkBook pata busca e divulgação de serviços.


Orientações para execução do projeto em uma máquina local.

1 - Clone esse repositório.

2 - Crie um virtualenv com Python 3.

3 - Ative o virtualenv.

4 - Instale as dependências.

5 - Rode as migrações.

6 - Rode o projeto

**Windows:**

git clone https://github.com/CimaraOliveira/projetoWorkBook.git

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

**Linux:**

git clone https://github.com/CimaraOliveira/projetoWorkBook.git

sudo apt install python3-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

# Descrição

O software dispõe de um chat para a realização da comunicação entre profissionais e clientes, visualização das avaliações e informações relevantes sobre os profissionais para garantir confiabilidade e segurança ao contratar um serviço. Durante o desenvolvimento deste trabalho foram realizados estudos bibliográficos, levantamento de requisitos, pesquisas através de questionários com profissionais e clientes, para identificar os principais problemas enfrentados por este público-alvo, com a intenção de uma solução capaz de beneficiar todos os usuários.    

O software foi desenvolvido na linguagem **Python** com framework **Django**, além da utilização de uma **Api** para a comunicação back-end com front-end.

# Apresentação do Software

Existem dois tipos de usuários, clientes e profissionais, e por isso, algumas funcionalidades são restritas a papéis específicos, o que quer dizer que existem recursos 
que o profissional poderá ter acesso e o cliente não. Cada tipo de usuário terá sua visão sob perspectivas diferentes. 

**Tela inicial do sistema**
![](https://github.com/CimaraOliveira/projetoWorkBook/blob/master/imagens/figura1.png)



**Tela de cadastro do usuário**
![](https://github.com/CimaraOliveira/projetoWorkBook/blob/master/imagens/figura3.png)

**Tela de login**                                       
![](https://github.com/CimaraOliveira/projetoWorkBook/blob/master/imagens/figura2.png)

**Tela home do cliente**
![](https://github.com/CimaraOliveira/projetoWorkBook/blob/master/imagens/figura7.png)

**Tela de perfil profissional**
![](https://github.com/CimaraOliveira/projetoWorkBook/blob/master/imagens/figura8.png)

**Tela home do profissional**
![](https://github.com/CimaraOliveira/projetoWorkBook/blob/master/imagens/figura4.png)

**Tela de caixa de entrada e envio de mensagens**
![](https://github.com/CimaraOliveira/projetoWorkBook/blob/master/imagens/figura6.png)

**Tela de avaliações profissionais**
![](https://github.com/CimaraOliveira/projetoWorkBook/blob/master/imagens/figura5.png)



 
                                      





