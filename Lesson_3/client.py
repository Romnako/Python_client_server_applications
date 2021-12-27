import chat
import jim

if __name__ == '__main__':
    client_name = input('Input name: ')

    parser = chat.create_parser()
    namespace = parser.parse_args()

    socket = chat.get_client_socket(namespace.addr, namespace.port)

    serv_addr = socket.getpeername()
    print(f'Connected to server: {serv_addr[0]}:{serv_addr[1]}')

    jim.PRESENCE['user']['account_name'] = client_name
    chat.send_data(socket, jim.PRESENCE)

    while True:
        data = chat.get_data(socket)

        if data['response'] != '200':
            break

        msg = input('Input message ("exit" for exit): ')
        jim.MESSAGE['message'] = msg
        chat.send_data(socket, jim.MESSAGE)

    socket.close()
