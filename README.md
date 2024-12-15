Updated version of the script [script](https://github.com/ericwoolard/Subreddit-Flair-Distribution-Counter) originally written by [@ericwoolard](https://github.com/ericwoolard)

REQUIREMENTS
------------
1. [Python 3](https://www.python.org/downloads/)
2. [Praw 4.x (or newer)](https://praw.readthedocs.io/en/latest/)
3. Reddit account with Moderator privileges for a subreddit
4. Client ID and Secret to supply with the script

REQUISITOS
------------
1. [Python 3](https://www.python.org/downloads/)

   Para verificar qual versão do Python está sendo usada ao rodar `python` no CMD, execute `python -V`. Da mesma forma, você pode verificar se o Python 3 está instalado corretamente e usando a versão correta com `python3 -V`. Se você tiver apenas uma versão do Python instalada, isso não se aplica a você.

2. [Praw 4.x (ou mais recente)](https://praw.readthedocs.io/en/latest/)
3. Conta no Reddit com privilégios de Moderador para um subreddit
4. ID do Cliente e Segredo para fornecer com o script

---

How to use
----------
1. Place the script and cfg file in a new folder by itself.
2. Edit lines 3-7 of the cfg file with your Client-ID, Client Secret, password, username and subreddit name, respectively (**DON'T** wrap these credentials in quotes like a typical string).
3. Start the script *from within the folder you saved it to* by entering `python main.py` in CMD. 
**Note** - From your command prompt, you will need to `cd` (Change Directory command) into the directory where the script is saved. See the tip below if you don't know how to do this.

Como usar
----------
1. Coloque o script e o arquivo cfg em uma nova pasta isolada.
2. Edite as linhas 3-7 do arquivo cfg com seu Client-ID, Client Secret, senha, nome de usuário e nome do subreddit, respectivamente (**NÃO** coloque essas credenciais entre aspas como uma string típica).
3. Execute o script *dentro da pasta onde você o salvou* digitando `python main.py` no CMD.  
**Nota** - A partir do seu prompt de comando, você precisará usar o comando `cd` (mudar de diretório) para a pasta onde o script está salvo. Veja a dica abaixo se não souber como fazer isso.

**Erro HTTP 401 (não autorizado)** -  
  * Isso geralmente significa que há um problema com o Client-ID fornecido. Quando você vai em preferências>apps e clica em 'editar' 
  sob o aplicativo que você criou, seu Client-ID estará [aqui](https://i.imgur.com/n3dKYcF.png)

**OAuthException: erro ``unauthorized_client`` ao processar a solicitação (Somente aplicativos de script podem usar autenticação por senha)** -  
  * Se você ver esse erro, é provável que não tenha criado o aplicativo corretamente em preferências > apps. Ao configurar isso,
  existem 3 opções para escolher: web app, installed app, script. Você *precisa* registrar o aplicativo como um **aplicativo de script** para que isso funcione. [Exemplo](https://i.imgur.com/ZV30NVg.png)

