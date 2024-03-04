def bubbleSort(arr: Array[Int]): Array[Int] = {
  val n = arr.length
  for (i <- 0 until n) {
    for (j <- 0 until n - i - 1) {
      if (arr(j) > arr(j + 1)) {
        val temp = arr(j)
        arr(j) = arr(j + 1)
        arr(j + 1) = temp
      }
    }
  }
  arr
}

// Example usage
val arr = Array(64, 34, 25, 12, 22, 11, 90)
val sortedArr = bubbleSort(arr)
println(sortedArr.mkString(", "))
