#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// Define a maximum number of students
#define MAX_STUDENTS 10

// Structure to store student information
struct Student {
    char name[64];
    int isPresent; // 1 for present, 0 for absent
};

int numStudents = 0;

int readint(){
    char buf[0x10];
    return atoi(fgets(buf,0x10,stdin));
}

// Function to display the menu
void displayMenu() {
    printf("\nAttendance System Menu:\n");
    printf("1. Mark Student as Present\n");
    printf("2. Mark Student as Absent\n");
    printf("3. View Attendance Status\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(120);
}

int main() {
	init();
	char studentName[64];
	struct Student students[MAX_STUDENTS];
	
    int choice;
    do {
        displayMenu();
        choice = readint();

        switch (choice) {
            case 1: // Mark Student as Present
                if (numStudents < MAX_STUDENTS) {
                    printf("Enter the name of the student: ");
                    students[numStudents].name[read(0,students[numStudents].name,64)-1]='\x00';
                    students[numStudents].isPresent = 1;
                    numStudents++;
                    printf("Student marked as present.\n");
                } else {
                    printf("Maximum number of students reached.\n");
                }
                break;
            case 2: // Mark Student as Absent
                if (numStudents > 0) {
                    printf("Enter the name of the student to mark as absent: ");
                    
                    scanf("%s", studentName);
                    getchar();
                    int found = 0;
                    for (int i = 0; i < numStudents; i++) {
                        if (strcmp(students[i].name, studentName) == 0) {
                            students[i].isPresent = 0;
                            found = 1;
                            printf("Student marked as absent.\n");
                            break;
                        }
                    }
                    if (!found) {
                        printf("Student not found.\n");
                    }
                } else {
                    printf("No students to mark as absent.\n");
                }
                break;
            case 3: // View Attendance Status
                printf("Attendance Status:\n");
                for (int i = 0; i < numStudents; i++) {
                    printf("No.%p %s : %s\n", &students[i].name, students[i].name, students[i].isPresent ? "Present" : "Absent");
                }
                break;
            case 4: // Exit
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice. Please select a valid option.\n");
                break;
        }
    } while (choice != 4);

    return 0;
}
