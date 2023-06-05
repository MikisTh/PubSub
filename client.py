import socket 

ip = '0.0.0.0'
port = 50000

client = socket.socket(socket.AF_INET, socket.SOCKE_STREAM)

try: 
   client.connect((ip, port))
   username = input ('Usuario>')
   print ('Conectado ao servidor!!\n')

except:
       return print ('\n Nao foi possivel se conectar ao servidor!\n') 

namefile = str(input('Arquivo>'))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print (f'{} Arquivo Recebido!\n')