import socket

eleccion = input("Quieres enviar (1) o recibir (2) mensajes?: ")
sock = socket.socket()


if (eleccion == "1"):           #Esto es para conectarse una conexion

    host = input("Especifica un equipo: ")
    port = int(input("Especifica un puerto: "))

    sock.connect((host, port))         #Esto inicia una conexion
    print(f"Conectado con {host}:{port}\n")


    while True:
        message = input("Envia un mensaje: ")

        if message == "quit":
            print("bye")
            sock.close()       #Esto cierra la conexion si el mensaje es quit
            break
        else:
            sock.send(message.encode('utf-8'))      #Esto manda el mensaje al servidor encodeado en utf-8

elif (eleccion == "2"):        #Esto es para escuchar

    host = "127.0.0.1"
    port = int(input("Especifica un puerto de escucha: "))


    sock.bind((host, port))     #Estas dos lineas inician una eschucha
    sock.listen(1)
    print(f"Escuchando en {host}:{port}")

    while True:
        conn, addr = sock.accept()     #Esto esto declara la variable addr que contiene la ip del cliente y la conn que son los datos de la conexion
        addr = addr[0]
        try:
            print(f'Conexión con {addr}\n Esperando a los mensajes...')
            while True:
                datos = conn.recv(4096)             #Esta variable almacena el mensaje recibido
                mensaje = datos.decode('UTF-8')
                if datos:
                    print(f'Recibido: {mensaje}')         #Esto muestra el mensaje decodeado
                else:
                    print(f'\nConexion con {addr} finalizada.')
                    sock.close      #Esto hace que cuando se termine la conexion
                    break
        finally:
            print("Saliendo...")
            break


else:
    print("Eso no es nunguna opicon, o 1 o 2 no mas.")