import socket 

ip = '0.0.0.0'
port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((ip, port))
    server.listen(50000)

   
    connection, adress = server.accept()
    print 'Estabelecendo conexao' %(ip, port)

    (obj, cliente) = server.accept()
    print 'Conexao estabelecida' %cliente[0]

    while True:
        msg = obj.recv(1024)
        if msg == 'Subscriber':
            print 'Voce entrou no modo subscriber'
            else msg == 'publisher': 
                print'Voce entrou no modo publisher':


        namefile = connection.recv(1024).decode()
    with open (namefile, 'rb') as file:
        for data in file.readlines():
            connection.send(data)

            print ('Arquivo enviado!')




except Exception as erro:
       print 'Comando invalido'
    server.close()