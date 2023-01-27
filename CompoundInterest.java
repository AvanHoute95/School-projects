import java.text.NumberFormat;
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
        NumberFormat formatter = NumberFormat.getCurrencyInstance();
        Scanner input = new Scanner(System.in);

        double futureValue;  // This is the future value
        double principal;  // This is the initial investment
        double interestRate;  // This is the interestRate rate in decimal format
        int numberOfYears;  // This is the number of years
        double interestAccrued;  // this is the interest accrued

        // This block of code collects information from the user
        System.out.print("Principal value: $");
        principal = input.nextDouble();
        System.out.print("Interest rate (ex. .09 for 9%): ");
        interestRate = input.nextDouble();
        System.out.print("Number of years: ");
        numberOfYears = input.nextInt();

        // Calculate the future value
        futureValue = principal * Math.pow((1 + interestRate), numberOfYears);
        String finalValue = formatter.format(futureValue);

        // Calculate the interest accrued
        interestAccrued = futureValue - principal;
        String interestAccumulated = formatter.format(interestAccrued);

        // Display results
        System.out.printf("Accumulated value after %d years: " + finalValue, numberOfYears);
        System.out.println();
        System.out.print("Interest accrued: " + interestAccumulated);
    }
}

