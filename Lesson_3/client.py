from chat import send_data, get_client_socket, get_data, create_parser
from jim import MESSAGE, PRESENCE

if __name__ == '__main__':
    client_name = input('Input name: ')

    parser = create_parser()
    namespace = parser.parse_args()

    socket = get_client_socket(namespace.addr, namespace.port)

    serv_addr = socket.getpeername()
    print(f'Connected to server: {serv_addr[0]}:{serv_addr[1]}')

    PRESENCE['user']['account_name'] = client_name
    send_data(socket, PRESENCE)

    while True:
        data = get_data(socket)

        if data['response'] != '200':
            break

        msg = input('Input message ("exit" for exit): ')
        MESSAGE['message'] = msg
        send_data(socket, MESSAGE)

    socket.close()
