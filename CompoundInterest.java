import java.util.Scanner;

/**
 * Compound interest calculator
 */
public class CompoundInterest
{
    /**
     * This program calculates compound interest
     */
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        double futureValue;  // This is the future value
        double principal;  // This is the initial investment
        double interestRate;  // This is the interestRate rate in decimal format
        int numberOfYears;  // This is the number of years
        double interestAccrued;  // this is the interest accrued

        System.out.print("Principal value: $");
        principal = input.nextDouble();
        System.out.print("Interest rate (ex. .09 for 9%): ");
        interestRate = input.nextDouble();
        System.out.print("Number of years: ");
        numberOfYears = input.nextInt();

        // Calculate the future value
        futureValue = principal * Math.pow((1 + interestRate), numberOfYears);

        // Calculate the interest accrued
        interestAccrued = futureValue - principal;

        // Display results
        System.out.printf("Accumulated value after %d years: $%.2f", numberOfYears, futureValue);
        System.out.println();
        System.out.printf("Interest accrued: $%.2f", interestAccrued);
    }
}

