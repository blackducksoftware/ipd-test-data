public class ShellSort {
    
    public static void shellSort(int[] array) {
        int n = array.length;
        
        for (int gap = n/2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                int temp = array[i];
                int j;
                
                for (j = i; j >= gap && array[j - gap] > temp; j -= gap) {
                    array[j] = array[j - gap];
                }
                
                array[j] = temp;
            }
        }
    }
    
    public static void main(String[] args) {
        int[] array = {12, 34, 54, 2, 3};
        
        System.out.println("Array before sorting:");
        for (int num : array) {
            System.out.print(num + " ");
        }
        
        shellSort(array);
        
        System.out.println("\nArray after sorting:");
        for (int num : array) {
            System.out.print(num + " ");
        }
    }
}
