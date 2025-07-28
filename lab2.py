from socket import *
import base64

# Учетные данные
email_from = "lettiev@cs.petrsu.ru"
password = "ohqu8juG"
email_to = "lettiev@cs.petrsu.ru"

# Содержимое письма
subject = "Тестовое письмо"
msg = "привет."
endmsg = "\n." #\r\n обозначают конец строки

# Подключение к серверу
mailserver = ("mail.cs.karelia.ru", 25)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

# Приветствие от сервера, recv будет содержать строку с данными, которые были получены от сервера
recv = clientSocket.recv(1024).decode()
print(recv)

# HELO  используется в протоколе SMTP для инициации связи между клиентом и сервером
clientSocket.send("HELO mail.cs.karelia.ru\r\n".encode())
recv = clientSocket.recv(1024).decode()
print(recv)



# Аутентификация
# Отправка команды AUTH LOGIN для инициирования процесса аутентификации
clientSocket.send("AUTH LOGIN\r\n".encode())
# Получение ответа от сервера, который может содержать информацию о том, что он готов к аутентификации
recv = clientSocket.recv(1024).decode()
print(recv)

# Отправка адреса электронной почты, закодированного в формат base64
clientSocket.send(base64.b64encode(email_from.encode()) + b"\r\n")
# Получение ответа от сервера после отправки адреса электронной почты
recv = clientSocket.recv(1024).decode()
print(recv)

# Отправка пароля, закодированного в формат base64
clientSocket.send(base64.b64encode(password.encode()) + b"\r\n")
# Получение ответа от сервера после отправки пароля
recv = clientSocket.recv(1024).decode()
print(recv)


# MAIL FROM
clientSocket.send(f"MAIL FROM:<{email_from}>\r\n".encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# RCPT TO
clientSocket.send(f"RCPT TO:<{email_to}>\r\n".encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# DATA
clientSocket.send("DATA\r\n".encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Сборка и отправка письма
email_message = f"""From: {email_from}
To: {email_to}
Subject: {subject}
MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 8bit

mime
QUIT
{msg}
.
MAIL FROM:<lettiev@cs.petrsu.ru>
RCPT TO:<lettiev@cs.petrsu.ru>
DATA
asdasda
.
"""
clientSocket.send(email_message.encode("utf-8"))
clientSocket.send("email_message".encode("utf-8"))
clientSocket.send("email_message".encode("utf-8"))
clientSocket.send("email_message".encode("utf-8"))





# Завершение сообщения
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# QUIT
clientSocket.send("QUIT\r\n".encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Закрытие соединения
clientSocket.close()