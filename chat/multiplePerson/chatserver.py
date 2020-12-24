# -*- encoding : utf-8 -*-
"""
@File       : chatserver.py
@Time       :2020/12/24 10:58
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import logging
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('127.0.0.1', 9999)
    s.bind(addr)

    user = {}

    while True:
        try:
            data, address = s.recvfrom(1024)
            if not address in user:
                for addr in user:
                    s.sendto("{} 进入聊天室……".format(data).encode('utf-8'), addr)
                user[address] = data.decode('utf-8')

            if 'EXIT'.lower() in data.decode('utf-8'):
                name = user[address]
                user.pop(address)
                for addr in user:
                    s.sendto("{} 离开了聊天室……".format(name).encode('utf-8'), addr)
            else:
                print("{} from {}:{}".format(data.decode('utf-8'), addr[0], addr[1]))
                for addr in user:
                    if addr != address:
                        s.sendto(data, addr)

        except ConnectionResetError:
            logging.warning("Someone left unexcept.")


if __name__ == '__main__':
    main()


