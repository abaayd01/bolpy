import logging
import bolpy.server as bp_server

if __name__ == '__main__':
    logging.basicConfig()
    bp_server.Server.start()
