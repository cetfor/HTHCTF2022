#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char** argv)
{
    char flag[64];
    char inputString[128];

    memset(&flag, 0, 64);
    memset(&inputString, 0, 128);
    
    FILE *fp = fopen("flag.txt", "r");
    if (fp != NULL) {
        size_t newLen = fread(flag, sizeof(char), 63, fp);
        if ( ferror( fp ) != 0 ) {
            fputs("Error reading file. Please report this to the CTF organizers!\n", stderr);
        } else {
            flag[newLen++] = '\0';
        }
        fclose(fp);
    }
    
    // prompt user
    fputs("Welcome to the repeater service! I repeat whatever you type. I'm perfect for those that love to hear themselves talk!\n", stdout);
    fputs("What would you like me to repeat? >> ", stdout);
    fflush(stdout);

    // get command remove newline chars
    fgets(inputString, 128, stdin);
    inputString[strcspn(inputString, "\r\n")] = 0;

    // repeat the user
    printf(inputString);
    
    puts("\nThanks for listening to yourself!\n");
    return EXIT_SUCCESS;
}
