# WhatsApp Bot - Webcrawling com Python e Selenium

Repositório contendo o protótipo de um bot para envio de mensagens automáticas no WhatsApp Web, utilizando a linguagem Python e a biblioteca Selenium para realizar o webcrawling.

---
## Requisitos

- [Python 3.x](https://www.python.org/downloads/): Linguagem de programação do código
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/): Necessário para a biblioteca selenium realizar as automações (Webcrawling)

## Instalação

Com o python instalado, abra o terminal e crie um [ambiente virtual](https://docs.python.org/3/library/venv.html). Com o ambiente ativado, instale as dependências necessárias:

```bash
pip install -r requirements.txt --no-cache-dir
```

**Obs.:** *Garanta que o ChromeDriver esteja nas variáveis de ambiente antes de executar o código!*

---
## Execução

Antes de executar o código, preencha os campos no arquivo `main.py`:

```python
contact_name = "<Nome do contato ou grupo>"
msg_to_send = "<Mensagem a ser enviada>"
msg_to_wait = "<Mensagem que o bot deve esperar antes de enviar a mensagem acima>"
```

Para iniciar o bot, basta executar o comando no terminal:

```bash
python main.py
```

---
## Referências

- [Selenium documentation](https://www.selenium.dev/documentation/)