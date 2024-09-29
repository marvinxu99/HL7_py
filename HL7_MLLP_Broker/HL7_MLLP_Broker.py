# Simple Python script to open a TCP connection send a test HL7 v2.4 message using MLLP
# https://gist.github.com/mnadjit
import socket
from datetime import datetime
import json
import uuid
    
class Ack:
    def __init__(self, msg_str: str):
        self.senderApp = msg_str.split('|')[4]
        self.senderFac = msg_str.split('|')[5]
        self.RecvApp = msg_str.split('|')[2]
        self.RecvFac = msg_str.split('|')[3]
        self.triggerEvent = msg_str.split('|')[8].split('^')[1]
        self.msgControlId = msg_str.split('|')[9]
        self.processingId = msg_str.split('|')[10]
        self.hL7Version = msg_str.split('|')[11]
    def get_string(self):
        return f"\
MSH|^~\\&|{self.senderApp}|{self.senderFac}|{self.RecvApp}|{self.RecvFac}|{current_datetime}||ACK^{self.triggerEvent}\
|{uuid.uuid4().hex}|{self.processingId}|{self.hL7Version}|||AL|NE{SEGMENT_TERMINATOR}MSA|AA|{self.msgControlId}"

with open('./config.json') as configFile:
    config = json.load(configFile)

LOCAL_HOST = config['LocalHost']
LOCAL_PORT = config['LocalPort']
REMOTE_IP = config['RemoteHost']
REMOTE_PORT = int(config['RemotePort'])
TcpTimeoutSecs = int(config['TcpTimeoutSeconds'])
HEADER = bytes.fromhex(config['Header'])
TRAILER = bytes.fromhex(config['Trailer'])
SEGMENT_TERMINATOR = bytes.fromhex(config['SegmentTerminator']).decode()
MSG_CODE = config['Message']['MessageCode']
TRIGGER_EVENT = config['Message']['TriggerEvent']
PROCESSING_ID = config['Message']['ProcessingID']
SENDR_APP = config['Message']['SendingApplication']
SENDR_FAC = config['Message']['SendingFacility']
RECV_APP = config['Message']['ReceivingApplication']
RECV_FAC = config['Message']['ReceivingFacility']
PAT_UR = config['Message']['PatientUR']
PAT_NAME = config['Message']['PatientName']

current_datetime = datetime.now().isoformat().replace('-','').replace('T','').replace(':','')[:14]

msg = f"\
MSH|^~\\&|{SENDR_APP}|{SENDR_FAC}|{RECV_APP}|{RECV_FAC}|{current_datetime}||{MSG_CODE}^{TRIGGER_EVENT}|{uuid.uuid4().hex}|{PROCESSING_ID}|2.4|||AL|NE{SEGMENT_TERMINATOR}\
EVN|{TRIGGER_EVENT}|{current_datetime}||APPAT_I|{SEGMENT_TERMINATOR}\
PID|1||{PAT_UR}^^^{RECV_FAC}^MR||{PAT_NAME}^^^MS^^L|{SEGMENT_TERMINATOR}\
PV1||I{SEGMENT_TERMINATOR}\
PV2|"

def main():
    print("MLLP server (s) or client (c)?")
    mode = input("> ")

    if not mode in ["s","c"]: # check if mode is valid
        print("Invalid mode")
        exit()

    if mode == "s":
        listen()

    elif mode == "c":
        connect_to_server()
        

def listen():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #local_port = input("...Port to listen on: ")
        # s.settimeout(TcpTimeoutSecs)
        local_ip = "127.0.0.1"
        if LOCAL_HOST != "":
            local_ip = LOCAL_HOST
        print("......listening for connections on", local_ip, ":", LOCAL_PORT)
        
        try:
            # Bind the socket to the port
            s.bind((local_ip, int(LOCAL_PORT)))
            # Listen for incoming connections
            s.listen(1)
            # Accept the connection
            client_socket, addr = s.accept()
            client_socket.settimeout(TcpTimeoutSecs)
            print("......connection accepted from", addr)
            print(colored(30, 255, 20, datetime.now()))

            # Receive data from the client
            msg_str = "" # initialize message string      

            while True:
                data = client_socket.recv(16384)        
                if data != "":
                    msg_str += data.decode('utf-8')
                if len(data) < 16384: 
                    break
        except Exception as e:
            print("......connection failed. Reason:", e)
            s.close()
            listen()

        # Remove Header, Trailer and Segment Terminator from the message and print it
        print("...received message:\n")    
        msg_str = msg_str.replace(HEADER.decode(), '').replace(TRAILER.decode(), '')
        for x in msg_str.split(SEGMENT_TERMINATOR):
            print(x)

        # Generate and send ACK message back to the client
        try:
            ack = Ack(msg_str).get_string()
            client_socket.sendall(HEADER + bytearray(ack, 'utf8') + TRAILER)

            print('\n\n...ACK message sent back to the client:')
            for x in ack.split(SEGMENT_TERMINATOR):
                print(x)
        except:
            print(colored(230, 20, 30, "Error while sending the acknowledgement message back to the sender."))
        finally:
            s.close()
            print()
            print('...connection closed. Listening for a new connection...')
            print()
            listen()

def connect_to_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        remote_ip = input("...IP or hostname to connect to <default: RemotHost value in config file>: ")
        remote_port = input("...Port to connect to <default: RemotePort value in config file>: ")
        if remote_ip == "":
            remote_ip = REMOTE_IP
        if remote_port == "":
            remote_port = REMOTE_PORT                
        print('\n...connecting to server [' + remote_ip + '] on port [' + str(remote_port) + ']')
        try:
            # Connect to remote server
            s.connect((remote_ip, int(remote_port)))
            print('......successfully connected to server')

            # Print the message to be sent
            print('...sending message:')
            for x in msg.split(SEGMENT_TERMINATOR):
                print(x)

            # Send the message to the server
            s.sendall(HEADER + bytearray(msg, 'utf8')  + TRAILER)
            print('\n...message sent.') 
        except Exception as e:
            print("......connection failed. Reason:", e)
            print()
            exit()

        # Get response from the server and print it
        while True:
            try:
                response = s.recv(4096)
                responseStr = response.decode('utf-8')
                responseStr = responseStr.replace(HEADER.decode(), '').replace(TRAILER.decode(), '')
                print('\n...response received:')
                for x in responseStr.split(SEGMENT_TERMINATOR):
                    print(x)
                break
            except Exception as e:
                print('\n...issue with receiving response back from the server. Reason:', e)
                break

        # CLOSE CONNECTION
        print('...closing the connection.\n')
        s.close()
        print('...connection closed.\n')
                  
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

if __name__ == '__main__':
    main()