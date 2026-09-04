#include <stdio.h>
#include<string.h>

/* Global Variables */
int totalSeats = 50;
int availableSeats = 50;
int busNumber = 101;

void login();
void menu();
void bookTicket();
void cancelTicket();
void checkStatus();

int main() {
    login();
    return 0;
}

void login() {
    char username[20], password[20];
    int choice;

    printf("***** BUS RESERVATION SYSTEM *****\n");
    printf("1. Login\n");
    printf("2. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("Enter Username: ");
        scanf("%s", username);
        printf("Enter Password: ");
        scanf("%s", password);

        printf("\nLogin Successful! Welcome, %s\n", username);
        menu();
    }
}

/* Menu Function */
void menu() {
    int choice;

    do {
        printf("\n=== User Menu ===\n");
        printf("1. Book Ticket\n");
        printf("2. Cancel Ticket\n");
        printf("3. Check Bus Status\n");
        printf("4. Logout\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                bookTicket();
                break;
            case 2:
                cancelTicket();
                break;
            case 3:
                checkStatus();
                break;
            case 4:
                printf("Logout Successful!\n");
                break;
            default:
                printf("Invalid Choice!\n");
        }
    } while (choice != 4);
}

/* Book Ticket Function */
void bookTicket() {
    int seats;
    printf("Enter number of seats to book: ");
    scanf("%d", &seats);

    if (seats <= availableSeats) {
        availableSeats = availableSeats - seats;
        printf("Booking Successful!\n");
    } else {
        printf("Not enough seats available!\n");
    }
}

/* Cancel Ticket Function */
void cancelTicket() {
    int seats;
    printf("Enter number of seats to cancel: ");
    scanf("%d", &seats);

    availableSeats = availableSeats + seats;
    if (availableSeats > totalSeats)
        availableSeats = totalSeats;

    printf("Cancellation Successful!\n");
}

/* Check Status Function */
void checkStatus() {
    printf("\nBus Number: %d\n", busNumber);
    printf("Source City: Delhi\n");
    printf("Destination City: Bihar\n");
    printf("Total Seats: %d\n", totalSeats);
    printf("Available Seats: %d\n", availableSeats);
    printf("Fare: 500\n");
}

