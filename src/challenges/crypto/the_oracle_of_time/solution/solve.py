import argparse
import socket
import time

def connect():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 7602
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    return s

def main():
    BUFFER_SIZE = 1024
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz_HTH}{'
    last_check_time = 0
    guess = "------------------------\n"
    
    # by observation, we know the challenge server wants 24 characters
    for i in range(0, 24):
        
        # we're merely guessing the valid characters in a flag, we could make this alphabet more complex to try more characters
        for char in alphabet:

            # connect to the challenge
            s = connect()
            
            # get the challenge banner and submission prompt
            data = s.recv(BUFFER_SIZE)
            
            # send our guess for analysis
            guess = list(guess)
            guess[i] = char
            guess = ''.join(guess)

            print("Checking input: {}".format(guess[:-1]))
            start = time.time()
            s.send(bytes(guess, 'utf-8'))
            while data:
                data = s.recv(BUFFER_SIZE)
            end = time.time()
            delta = end - start
            
            print("Delta: {0:.2f}".format(delta))
            if delta > (last_check_time + 0.20):
                last_check_time += delta
                s.close()
                break
            
            last_check_time = delta
            s.close()

if __name__ == "__main__":
    main()
