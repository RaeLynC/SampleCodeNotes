#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include "../include/threadtest.h"

int sharedCtr = 0;
int sharedCtrUnprotected = 0;
extern pthread_cond_t tcond;
extern pthread_mutex_t tmutex;
extern int done;

void tCleanup(void *arg) {
    pthread_mutex_unlock(&tmutex);
}

void *tTest_t(void *parg) {
    char *param = (char *)parg;
    char local_id = *param;

    printf("T[%c] Created\n", local_id);
    while (!done) {
        sleep(1);

        pthread_mutex_lock(&tmutex);
        pthread_cleanup_push(tCleanup, NULL);
        pthread_cond_wait(&tcond, &tmutex);
        ++sharedCtr;
        pthread_cleanup_pop(1);

        ++sharedCtrUnprotected;
        printf("T[%c] = global (%d) local (%d)\n", 
            local_id, sharedCtr, sharedCtrUnprotected);
    }

    return NULL;
}
