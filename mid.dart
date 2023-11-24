import 'dart:io';
import 'dart:math';

void main() {
  // print("${c.maxSpeed} , ${c.model}");

  var c2 = Car.maxSpeed(100);
  // var c = Car("Test");

  print("${c2.maxSpeed} , ${Car.model}");
}

// 0 1 1 2 3 5 8
// 2 3 5 7 9 11 13
int fib([int n = 2]) {
  return n < 2 ? n : fib(n - 1) + fib(n - 2);
}

void pNumbers(int end) {
  for (int i = 2; i <= end; i++) {
    bool prime = true;
    for (int j = 2; j <= sqrt(i); j++) {
      if (i % j == 0) {
        prime = false;
        break;
      }
    }
    if (prime) stdout.write("$i , ");
  }
}

class Car {
  static String model = "";
  int maxSpeed = 0;
  Car(String model, [int maxSpeed = 100]) {
    Car.model = model;
    this.maxSpeed = maxSpeed;
  }
  Car.modelConst(String model) : this(model);
  Car.maxSpeed(int maxSpeed) : this(Car.model = "Hussam", maxSpeed);
}
