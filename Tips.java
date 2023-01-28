import java.util.Scanner;

/**
 * A program to calculate the appropriate tip at a restaurant
 *
 * @author avanhoute21@georgefox.edu
 */
public class Tips
{
    /**
     *
     * @param service is the service level
     * @return the percentage of the tip
     */
    public static double getTip (String service)
    {
        // variables for tips
        final double GREAT = 0.25;
        final double GOOD = 0.20;
        final double OK = 0.15;
        final double BAD = 0.10;
        final double AWFUL = 0.0;
        double tipPercent = 0.0;

        // logic for finding tips
        if (service.equals("great"))
        {
            tipPercent = GREAT;
        }
        else if (service.equals("good"))
        {
            tipPercent = GOOD;
        }
        else if (service.equals("ok"))
        {
            tipPercent = OK;
        }
        else if (service.equals("bad"))
        {
            tipPercent = BAD;
        }
        else if (service.equals("awful"))
        {
            tipPercent = AWFUL;
        }
        return tipPercent;
    }

    /**
     * Main entry point to run the program
     *
     * @param args Command-line arguments (not used)
     */
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        // variables for the program are declared here
        double billAmount;
        String serviceLevel;
        double tipPercent;
        double tipAmount;
        double totalBill;
        double formattedTipPercent;

        // ask the user for information
        System.out.print("Enter the bill amount: ");
        billAmount = input.nextDouble();
        System.out.print("Enter the service level: ");
        serviceLevel = input.next();

        // perform calculations
        tipPercent = getTip(serviceLevel);
        formattedTipPercent = tipPercent * 100;
        tipAmount = billAmount * (tipPercent);
        totalBill = billAmount + tipAmount;
        System.out.println("------------------------------");

        // display results
        System.out.printf("The tip percent is %.0f%%", formattedTipPercent);
        System.out.println();
        System.out.printf("The tip amount is $%.2f", tipAmount);
        System.out.println();
        System.out.printf("The new total is $%.2f", totalBill);
    }
}
