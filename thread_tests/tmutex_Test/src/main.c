#include <stdlib.h>
#include <pthread.h>
#include <curses.h>
#include <term.h>
#include <unistd.h>
#include <../include/threadtest.h>

#define MAX_THREADS 2
pthread_t activeThreads[MAX_THREADS] = {0};
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
            if (!activeThreads[0]) {
                if (pthread_create(&activeThreads[0], NULL, tTest_t, (void *)&choice))
                    fprintf(stderr, "Thread creation err\n");
            }
            else
                printf("T1 already started\n");
            break;
        case 'b':
            if (!activeThreads[1]) {
                if (pthread_create(&activeThreads[1], NULL, tTest_t, (void *)&choice))
                    fprintf(stderr, "Thread creation err\n");
            }
            else
                printf("T2 already started\n");
            break;
        case 'c':
            clearScreen();
            break;
        case 'd':
            printf("activeThreads ");
            for (int i = 0; i < MAX_THREADS; i++)
                activeThreads[i] != 0 ? printf("[active] ") : printf("[0] ");
            printf("\n");
            break;
        case 'e':
            cleanup_threads();
            break;
        case 'f':
            printf("exit menu\n");
            cleanup_threads();
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
    printf("\ta. Start thread 1\n");
    printf("\tb. Start thread 2\n");
    printf("\tc. Clear screen\n");
    printf("\td. Show current state:\n");
    printf("\te. Reset all threads\n");
    printf("\tf. Exit\n");
    printf("Enter choice: \n");
    scanf(" %c", &choice);	// Note " %c" to ignore white space
    return choice;
}

void cleanup_threads() {
    void *res;

    done = 1;
    for (int i = 0; i < MAX_THREADS; i++) {
        if (activeThreads[i] != 0){
            if (pthread_cancel(activeThreads[i]))
                fprintf(stderr, "pthread_cancel (ERR)\n");
            else
                printf("\t[%d] canceled\n", i);
            if (pthread_join(activeThreads[i], &res))
                fprintf(stderr, "pthread_join (ERR)\n");
            else {
                if (res == PTHREAD_CANCELED)
                    printf("\t[%d] joined (CANCELED)\n", i);
                else
                    printf("\t[%d] joined (NORMAL EXIT)\n", i);
            }
            activeThreads[i] = 0;
        }
    }
    done = 0;
}
