#include <sys/socket.h>
#include <sys/types.h>
#include <sys/un.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define NSTRS       3           /* no. of strings  */
#define ADDRESS     "mysocket"  /* addr to connect */
#define ACK         "ACK"

/* Strings we send to the client. */
char *strs[NSTRS] = {
    "This is the first string from the server.\n",
    "This is the second string from the server.\n",
    "This is the third string from the server.\n"
};

int main()
{
    char c;
    FILE *fp;
    socklen_t fromlen;
    int s, ns, len;
    struct sockaddr_un server_saun, client_saun;

    /* 1. Get socket */
    if ((s = socket(AF_UNIX, SOCK_STREAM, 0)) < 0) {
        perror("server: socket");
        exit(1);
    }

    /* 2. Create bind-address */
    server_saun.sun_family = AF_UNIX;
    strcpy(server_saun.sun_path, ADDRESS);
    server_saun.sun_path[sizeof(server_saun.sun_path)-1] = '\0';

    /* 3. "Assign the address to the socket" - unlink the name first so 
     * that the bind won't fail. */
    unlink(ADDRESS);
    len = SUN_LEN(&server_saun);
    if (bind(s, (struct sockaddr *)&server_saun, len) < 0) {
        perror("server: bind");
        exit(1);
    }

    /* 4. Listen/Accept connections */
    if (listen(s, 5) < 0) {
        perror("server: listen");
        exit(1);
    }

    if ((ns = accept(s, (struct sockaddr *)&client_saun, &fromlen)) < 0) {
        perror("server: accept");
        exit(1);
    }

    /* Use stdio for reading the socket. */
    fp = fdopen(ns, "r");

    /* First we send some strings to the client. */
    for (int i = 0; i < NSTRS; i++)
        send(ns, strs[i], strlen(strs[i]), 0);

    char buffer[255];
    for (int i = 0; i < NSTRS; i++) {
        int msg_size = recv(ns, buffer, 255, 0);
        printf("recv (%d), (%s)\n", msg_size, buffer);
        send(ns, ACK, 4, 0);
    }

    /* Use close() to terminate the connection. */
    close(s);

    exit(0);
}
