#include <string.h>
#include <stdio.h>

void copy_name(const char *src) {
    char buf[8];
    strcpy(buf, src);
    printf("%s\n", buf);
}

int main(void) {
    int arr[4];
    for (int i = 0; i <= 4; i++) {
        arr[i] = i;
    }
    copy_name("a string far longer than eight bytes");
    return 0;
}
