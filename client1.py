import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    ordre_chanteurs = input("Entrez l'ordre des chanteurs : ")
    client.sendall(ordre_chanteurs.encode())
    choral = input("Entrez le chanteur sur lequel vous voulez la choral : ")
    client.sendall(choral.encode())
    resultat = client.recv(1024).decode()
    print(f"Résultat : {resultat}")





