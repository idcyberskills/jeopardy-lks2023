//gcc -g -Wl,-z,relro,-z,now -fstack-protector-all chall.c -o chall
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// Structure to represent user data

struct User {
    char username[50];
    char password[50];
    char role[50];
} ;

struct User *users[30];

int numUsers = 0; // Number of registered users

int readint(){
    char buf[0x10];
    return atoi(fgets(buf,0x10,stdin));
}

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

// Function to display the menu
void displayMenu() {
    printf("\nUser Management Menu:\n");
    printf("1. Login User\n");
    printf("2. Register User\n");
    printf("3. Delete User\n");
    printf("4. Feedback\n");
    printf("5. Exit\n");
}

// Function to handle user login
void loginUser() {
    char username[50];
    char password[50];
    int found = 0;

    printf("Enter your username: ");
    fgets(username,50,stdin);
    username[strlen(username)-1]=0;
    printf("Enter your password: ");
    fgets(password,50,stdin);
    password[strlen(password)-1]=0;

    for (int i = 0; i < numUsers; i++) {
        if (users[i]){
            if (strcmp(users[i]->username, username) == 0 && strcmp(users[i]->password, password) == 0) {
                found = 1;
                printf("Login successful. Welcome, %s (%s)!\n", username, users[i]->role);
                if (strcmp(users[i]->role,"admin") == 0){
                    printf("Hello Admin\n");
                    win();
                }
                break;
            }
        }
    }

    if (!found) {
        printf("Login failed. Incorrect username or password.\n");
    }
}

// Function to register a new user
void registerUser() {
    if (numUsers==30){
        return;
    }
    int index=-1;

    for (int i = 0; i < 30; ++i)
    {
        if (!users[i]){
            index=i;
            break;
        }
    }

    users[index] = (struct User *)malloc(sizeof(struct User));
    if (*users == NULL) {
        printf("Memory allocation error. Cannot register a new user.\n");
        exit(1);
    }

    printf("Enter your username: ");
    fgets(users[index]->username,50,stdin);
    users[index]->username[strlen(users[index]->username)-1]=0;
    printf("Enter your password: ");
    fgets(users[index]->password,50,stdin);
    users[index]->password[strlen(users[index]->password)-1]=0;

    strcpy(users[index]->role,"standard");

    printf("User registered successfully.\n");
    numUsers += 1;
}

void listUser() {
    // TODO
}

// Function to delete a user by username
void deleteUser() {
    if (numUsers == 0) {
        printf("No registered users to delete.\n");
        return;
    }

    char username[50];
    char password[50];
    int found = 0;

    printf("Enter the username of the user to delete: ");
    fgets(username,50,stdin);
    username[strlen(username)-1]=0;
    printf("Enter the password of the user to delete: ");
    fgets(password,50,stdin);
    password[strlen(password)-1]=0;

    for (int i = 0; i < 30; ++i)
    {
        if (users[i]){
            if (strcmp(users[i]->username, username) == 0 && strcmp(users[i]->password, password) == 0) {
                free(users[i]);
                printf("User '%s' deleted successfully.\n", username);
                found=1;
                break;
            }
        }
    }

    if (!found) {
        printf("User not found or Password incorrect. Deletion failed.\n");
    }
}

// Function to handle user feedback
void feedback() {
    int length;
    printf("Enter the length of feedback: ");
    length = readint();
    char *feedback = (char *)malloc(length + 1); // +1 for null-terminator

    if (feedback == NULL) {
        printf("Memory allocation error. Cannot provide feedback.\n");
        return;
    }

    printf("Enter your feedback (up to %d characters): ", length);
    fgets(feedback,length,stdin);

    printf("Feedback was successfully sent");

}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(120);

    users[0] = (struct User *)malloc(sizeof(struct User));
    strcpy(users[0]->username,"admin");
    strcpy(users[0]->password,"Gc6x51q1Pov7ZBMD29eOLyVowvahJ1");

    strcpy(users[0]->role,"admin");
    numUsers += 1;

}

int main() {
    init();
    
    int choice;
    do {
        displayMenu();
        printf("Enter your choice: ");
        choice = readint();

        switch (choice) {
            case 1: // Login User
                loginUser();
                break;

            case 2: // Register User
                registerUser();
                break;
            // case 3: // listUser
            //     listUser();
            //     break;

            case 3: // Delete User
                deleteUser();
                break;

            case 4: // Feedback
                feedback();
                break;

            case 5: // Exit
                printf("Exiting the program.\n");
                return 0;
                break;

            default:
                printf("Invalid choice. Please select a valid option.\n");
                break;
        }
    } while (choice != 5);

    return 0;
}
