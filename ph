<?php
// Define an associative array of countries and their capitals
$countries = array(
    "USA" => "Washington D.C.",
    "France" => "Paris",
    "Japan" => "Tokyo",
    "India" => "New Delhi"
);

// Loop through the associative array and print each country and its capital
foreach ($countries as $country => $capital) {
    echo "Country: $country, Capital: $capital <br>";
}

// Define a function to check if a number is prime
function isPrime($num) {
    if ($num <= 1) {
        return false;
    }
    
    for ($i = 2; $i <= sqrt($num); $i++) {
        if ($num % $i == 0) {
            return false;
        }
    }
    
    return true;
}

// Call the function to check if a number is prime
$number = 17;
if (isPrime($number)) {
    echo "$number is a prime number. <br>";
} else {
    echo "$number is not a prime number. <br>";
}

// Define a class with properties and methods
class Animal {
    public $name;
    public $sound;

    public function makeSound() {
        echo $this->name . " makes a sound: " . $this->sound . "<br>";
    }
}

// Create objects of the class and call the method
$animal1 = new Animal();
$animal1->name = "Dog";
$animal1->sound = "Woof";
$animal1->makeSound();

$animal2 = new Animal();
$animal2->name = "Cat";
$animal2->sound = "Meow";
$animal2->makeSound();
?>
