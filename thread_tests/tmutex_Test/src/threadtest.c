#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include "../include/threadtest.h"

int sharedCtr = 0;
pthread_t lockHolder = 0;
pthread_mutex_t tmutex = PTHREAD_MUTEX_INITIALIZER;
extern int done;

void tCleanup(void *arg) {
    if (lockHolder == pthread_self()) {
        pthread_mutex_unlock(&tmutex);
        printf("tCleanup:unlock\n");
    }
    else
        printf("tCleanup:no lock\n");
}

void *tTest_t(void *parg) {
    char *param = (char *)parg;
    char local_value = *param;
    int local_ctr = 0;

    while (!done) {
        sleep(1);

        printf("#Argument = %c\n", local_value);
        pthread_mutex_lock(&tmutex);
        pthread_cleanup_push(tCleanup, NULL);
        lockHolder = pthread_self();
        ++sharedCtr;
        local_ctr = sharedCtr;
        pthread_testcancel();
        pthread_cleanup_pop(1); // NOTE: executes tCleanup(), releases mutex

        printf("T[%c] = global (%d) local (%d)\n", 
            local_value, sharedCtr, local_ctr);
    }

    return NULL;
}
