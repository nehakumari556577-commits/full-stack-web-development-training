#include <stdio.h>
#include <string.h>

/* Bus Details */
int busNo = 101;
int total_seats = 50;
int available_seats = 50;
float fare = 500.00;

char sourceCity[20] = "Delhi";
char destinationCity[20] = "Bihar";

/* User Registration Details */
char regUsername[20];
char regPassword[20];

/* Function Declarations */
void registerUser();
void login();
void menu();
void bookTicket();
void cancelTicket();
void checkstatus();

int main()
{
    login();
    return 0;
}

/* Registration Function */
void registerUser()
{
    printf("\n===== USER REGISTRATION =====\n");
    printf("Create Username: ");
    scanf("%s", regUsername);
    printf("Create Password: ");
    scanf("%s", regPassword);
    printf("\nRegistration Successful! Please Login.\n");
}

/* Login Function */
void login()
{
    char username[20];
    char password[20];
    int choice;

    printf("\n******** BUS RESERVATION SYSTEM ********\n");
    printf("1. Register\n");
    printf("2. Login\n");
    printf("3. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1)
    {
        registerUser();
        login();
    }
    else if (choice == 2)
    {
        printf("\nEnter Username: ");
        scanf("%s", username);
        printf("Enter Password: ");
        scanf("%s", password);

        if (strcmp(username, regUsername) == 0 &&
            strcmp(password, regPassword) == 0)
        {
            printf("\nLogin Successful! Welcome %s\n", username);
            menu();
        }
        else
        {
            printf("\nInvalid Username or Password!\n");
            login();
        }
    }
    else
    {
        printf("\nThank you for using the system!\n");
    }
}

/* User Menu */
void menu()
{
    int choice;
    do
    {
        printf("\n========== USER MENU ==========\n");
        printf("1. Book Ticket\n");
        printf("2. Cancel Ticket\n");
        printf("3. Check Bus Status\n");
        printf("4. Logout\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            bookTicket();
            break;
        case 2:
            cancelTicket();
            break;
        case 3:
            checkstatus();
            break;
        case 4:
            printf("\nLogout Successful!\n");
            break;
        default:
            printf("\nInvalid Choice!\n");
        }
    } while (choice != 4);
}

/* Book Ticket */
void bookTicket()
{
    int seats;
    printf("\nEnter number of seats to book: ");
    scanf("%d", &seats);

    if (seats <= available_seats)
    {
        available_seats -= seats;
        printf("\nBooking Successful!");
        printf("\nTotal Fare: %.2f\n", seats * fare);
    }
    else
    {
        printf("\nNot enough seats available!\n");
    }
}

/* Cancel Ticket */
void cancelTicket()
{
    int seats;
    printf("\nEnter number of seats to cancel: ");
    scanf("%d", &seats);

    available_seats += seats;
    if (available_seats > total_seats)
        available_seats = total_seats;

    printf("\nCancellation Successful!\n");
}

/* Check Bus Status */
void checkstatus()
{
    printf("\n========== BUS STATUS ==========\n");
    printf("Bus Number       : %d\n", busNo);
    printf("Source City      : %s\n", sourceCity);
    printf("Destination City : %s\n", destinationCity);
    printf("Total Seats      : %d\n", total_seats);
    printf("Available Seats  : %d\n", available_seats);
    printf("Fare per Seat    : %.2f\n", fare);
}
