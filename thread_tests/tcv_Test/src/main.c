
#include <stdlib.h>
#include <pthread.h>
#include <curses.h>
#include <term.h>
#include <unistd.h>
#include <../include/threadtest.h>

#define MAX_THREADS 2
pthread_t waiters[MAX_THREADS] = {0};
pthread_cond_t tcond = PTHREAD_COND_INITIALIZER;
pthread_mutex_t tmutex = PTHREAD_MUTEX_INITIALIZER;
int done = 0;

/* Helper Functions */
void clearScreen();
char get_selection();
void cleanup_threads();

int main()
{
    clearScreen();
    
    char choice = get_selection();
    while (1) {
        switch (choice)
        {
        case 'a':
            if (!waiters[0]) {
                if (pthread_create(&waiters[0], NULL, tTest_t, (void *)&choice))
                    fprintf(stderr, "Thread creation err\n");
            }
            else
                printf("T1 already started\n");
            break;
        case 'b':
            if (!waiters[1]) {
                if (pthread_create(&waiters[1], NULL, tTest_t, (void *)&choice))
                    fprintf(stderr, "Thread creation err\n");
            }
            else
                printf("T2 already started\n");
            break;
        case 'c':
            clearScreen();
            break;
        case 'd':
            pthread_mutex_lock(&tmutex);
            pthread_cond_signal(&tcond);
            pthread_mutex_unlock(&tmutex);
            break;
        case 'e':
            pthread_mutex_lock(&tmutex);
            pthread_cond_broadcast(&tcond);
            pthread_mutex_unlock(&tmutex);
            break;
        case 'f':
            printf("exit menu\n");
            done = 1;
            exit(1);
            break;
        default:
            printf("INVALID selection: Please try again\n");
            choice = 0;
            break;
        }
    
        choice = get_selection();
    }

    return 0;
}

void clearScreen() {
    // Clear screen
    int result;
    setupterm(NULL, STDOUT_FILENO, &result);
    if (result <= 0) return;
    putp(tigetstr("clear"));
}

char get_selection() {
    char choice = 0;
    printf("\nSimple Thread Test w/FileIO:\n");
    printf("\ta. Start waiter 1\n");
    printf("\tb. Start waiter 2\n");
    printf("\tc. Clear screen\n");
    printf("\td. Signal waiters!\n");
    printf("\te. Broadcast waiters!\n");
    printf("\tf. Exit\n");
    printf("Enter choice: \n");
    scanf(" %c", &choice);	// Note " %c" to ignore white space
    return choice;
}
