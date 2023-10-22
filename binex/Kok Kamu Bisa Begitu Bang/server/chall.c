// gcc -g -Wl,-z,relro,-z,now -fstack-protector-all -no-pie chall.c -o chall
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int numGuests = 0;           // Number of guests checked in
int choice;
int roomNumber;

int readint(){
    char buf[0x10];
    return atoi(fgets(buf,0x10,stdin));
}

// Structure to store guest information
struct Guest {
    int roomNumber;
    char name[40];
    
};

void win(){
    FILE* file;
    int c = 0;

    file = fopen("flag.txt", "r");

    if (NULL == file) {
        fprintf(stderr, "Cannot open flag.txt");
        exit(EXIT_FAILURE);
    } else {
        while (1) {
            c = fgetc(file);
            if (c == EOF)
                break;
            putchar(c);
        }
        fclose(file);
    }   
}

// Function to check in a guest
void checkIn(struct Guest *guestList, int *numGuests) {
    if (*numGuests < 10) {
        printf("Enter guest name: ");
        read(0,guestList[*numGuests].name,41);

        printf("Enter room number: ");
        guestList[*numGuests].roomNumber = readint();

        (*numGuests)++;
        printf("Guest checked in successfully.\n");
    } else {
        printf("Sorry, the hotel is fully booked.\n");
    }
}

// Function to display guest list
void displayGuestList(const struct Guest *guestList, int numGuests) {
    if (numGuests > 0) {
        printf("Guest List:\n");
        for (int i = 0; i < numGuests; i++) {
            printf("Guest %d: %s, Room %d\n", i + 1, guestList[i].name, guestList[i].roomNumber);
        }
    } else {
        printf("No guests have checked in.\n");
    }
}

// Function to delete a guest by room number
void deleteGuest(struct Guest *guestList, int *numGuests, int roomNumber) {
    int found = 0;
    for (int i = 0; i < *numGuests; i++) {
        if (guestList[i].roomNumber == roomNumber) {
            found = 1;
            for (int j = i; j < *numGuests - 1; j++) {
                strcpy(guestList[j].name, guestList[j + 1].name);
                guestList[j].roomNumber = guestList[j + 1].roomNumber;
            }
            (*numGuests)--;
            printf("Guest with room number %d deleted.\n", roomNumber);
            break;
        }
    }
    if (!found) {
        printf("Guest with room number %d not found.\n", roomNumber);
    }
}

// Function to edit guest information
void editGuest(struct Guest *guestList, int numGuests, int roomNumber) {
    for (int i = 0; i < numGuests; i++) {
        if (guestList[i].roomNumber == roomNumber) {
            printf("Enter new guest name: ");
            scanf("%s", guestList[i].name);
            printf("Enter new room number: ");
            scanf("%d", &guestList[i].roomNumber);
            printf("Guest information updated.\n");
            return;
        }
    }
    printf("Guest with room number %d not found.\n", roomNumber);
}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(120);
}

int menu(){
    printf("\nHotel Management Menu:\n");
    printf("1. Check-in\n");
    printf("2. Display Guest List\n");
    printf("3. Delete Guest\n");
    printf("4. Edit Guest Information\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
    return readint();
}

int main() {
    init();
    struct Guest guestList[10];  // Array to store guest information


    while (1) {

        choice = menu();
        switch (choice) {
            case 1:
                checkIn(guestList, &numGuests);
                break;
            case 2:
                displayGuestList(guestList, numGuests);
                break;
            case 3:
                if (numGuests > 0) {
                    printf("Enter room number to delete: ");
                    roomNumber = readint();
                    deleteGuest(guestList, &numGuests, roomNumber);
                } else {
                    printf("No guests to delete.\n");
                }
                break;
            case 4:
                if (numGuests > 0) {
                    printf("Enter room number to edit: ");
                    roomNumber = readint();
                    editGuest(guestList, numGuests, roomNumber);
                } else {
                    printf("No guests to edit.\n");
                }
                break;
            case 5:
                printf("Exiting the program.\n");
                return 0;
            default:
                printf("Invalid choice.\n");
        }
    }

    return 0;
}

