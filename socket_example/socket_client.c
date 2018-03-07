#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define NSTRS       3           /* no. of strings  */
#define ADDRESS     "mysocket"  /* addr to connect */
#define ACK	    "ACK"

/* Strings we send to the server. */
char *strs[NSTRS] = {
    "Message\n",
    "Message can vary in length\n",
    "alot\n"
};

int main()
{
    char c;
    FILE *fp;
    int s, len;
    struct sockaddr_un saun;

    /* 1. Get socket */
    if ((s = socket(AF_UNIX, SOCK_STREAM, 0)) < 0) {
        perror("client: socket");
        exit(1);
    }

    /* 2. Create bind-address. */
    saun.sun_family = AF_UNIX;
    strcpy(saun.sun_path, ADDRESS);

    /* Try to connect to the address.  For this to succeed, 
     * the server must already have bound this address, and 
     * must have issued a listen() request. */
    len = SUN_LEN(&saun);
    if (connect(s, (const struct sockaddr *)&saun, len) < 0) {
        perror("client: connect");
        exit(1);
    }

    /* Use stdio for reading the socket. */
    fp = fdopen(s, "r");

    /* First we read some strings from the server and print them out. */
    for (int i = 0; i < NSTRS; i++) {
        while ((c = fgetc(fp)) != EOF) {
            putchar(c);
            if (c == '\n')
                break;
        }
    }

    /* Now we send some strings to the server. */
    char ack[4] = {0};
    for (int i = 0; i < NSTRS; i++) {
        printf("SEND: %lu size (%s)\n", strlen(strs[i]), strs[i]);
        send(s, strs[i], strlen(strs[i]), 0);
        /* Wait for ACK */
        int msg_size = recv(s, ack, 4, 0);
        printf("\tRX (%d bytes) (%s)\n", msg_size, ack); 
    }

    /* Use close() to terminate the connection. */
    close(s);

    exit(0);
}
