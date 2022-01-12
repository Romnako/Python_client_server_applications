from chat import send_data, get_server_socket, get_data, create_parser
from jim import SERV_RESP, RESPONSE

client_name = ''

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    socket = get_server_socket(namespace.addr, namespace.port)

    serv_addr = socket.getsockname()
    print(f'Server started at {serv_addr[0]}:{serv_addr[1]}')

    client, address = socket.accept()
    print(f'Client connected from {address[0]}:{address[1]}')

    while True:
        data = get_data(client)

        if client_name == '':
            if data['action'] == 'presence' and data['user']['account_name'] != '':
                client_name = data['user']['account_name']
                RESPONSE['response'], RESPONSE['alert'] = SERV_RESP[0]
                print(f'{data["time"]} - {data["user"]["account_name"]}: {data["user"]["status"]}')
            else:
                RESPONSE['response'], RESPONSE['alert'] = SERV_RESP[1]

        if client_name != '' and data['action'] == 'msg':
            print(f'{data["time"]} - {client_name}: {data["message"]}')
            RESPONSE['response'], RESPONSE['alert'] = SERV_RESP[2]

        send_data(client, RESPONSE)

        if RESPONSE['response'] != '200':
            client.close()
            break

    socket.close()