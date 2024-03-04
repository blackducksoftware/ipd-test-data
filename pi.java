import java.math.BigDecimal;
import java.math.RoundingMode;

public class CalculatePi {
    public static void main(String[] args) {
        int scale = 1000;
        BigDecimal pi = computePi(scale);
        System.out.println(pi);
    }

    private static BigDecimal computePi(int scale) {
        BigDecimal pi = BigDecimal.ZERO;
        BigDecimal term1 = BigDecimal.ONE;
        BigDecimal term2 = BigDecimal.ONE;
        BigDecimal term3 = BigDecimal.ONE;
        BigDecimal sign = BigDecimal.ONE;
        
        for (int i = 0; i < scale; i++) {
            BigDecimal divisor = new BigDecimal(2*i + 1);
            term1 = term1.multiply(new BigDecimal(i * 2));
            term2 = term2.multiply(new BigDecimal(i * 2 + 1));
            term3 = term3.multiply(new BigDecimal(i * 2 + 2));
            BigDecimal term = term1.multiply(term2).divide(term3.multiply(divisor), scale, RoundingMode.HALF_UP);
            
            if (i % 2 == 0) {
                pi = pi.add(term.multiply(sign));
            } else {
                pi = pi.subtract(term.multiply(sign));
            }
        }

        return pi.multiply(new BigDecimal(2));
    }
}
