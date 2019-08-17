from sys import exit
import signal


def exit_if_error(error):
    if error != None:
        print("Fuuuuuuu!!!", error)
        exit(666)


def wait_for_crl_c():
    def handler(sig, frame):
        print('Bye bye!')
        exit(0)

    signal.signal(signal.SIGINT, handler)
    print('Press Ctrl+C to stop')
