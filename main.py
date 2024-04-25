from WhatsappCrawler import WhatsappCrawler

if __name__ == "__main__":
    contact_name = "<Nome do contato ou grupo>"
    msg_to_send = "<Mensagem a ser enviada>"
    msg_to_wait = "<Mensagem que o bot deve esperar antes de enviar a mensagem acima>"

    wtpp_bot = WhatsappCrawler() # Cria o bot do WhatsApp para envio de mensagens 
    wtpp_bot.connect_smartphone() # Usuário precisa escanear o QR-Code
    wtpp_bot.set_contact(contact_name) # O bot irá clicar no contato ou grupo
    wtpp_bot.set_msg_to_send(msg_to_send) # O bot armazenará a mensagem que deve ser enviada
    wtpp_bot.wait_for_message(msg_to_wait) # O bot aguardará e enviará a mensagem
    # Caso queira que o bot não espere uma mensagem antes de enviar outra
    # Basta comentar a linha 12 e "descomentar" a linha 15
    # wtpp_bot.send_message()
    wtpp_bot.close_session() # Desconecta o Whatsapp e termina a execução do bot
