FakeRPi
=======

Develop for Raspberry Pi on Windows or other systems that don't have RPi.GPIO libraries.

It implements RPi.GPIO functions and return None values.

When we are developing on some IDE's, they will verify the code syntax and consequently report many errors as the library is not present on include paths. That can be annoying for the user, as they see a lot of errors everywhere and some red lines. With FakeRPi you can fix that and also benefits from code completion and some utilities.

This is not an emulator of Rasberry Pi!

## When to use

* Developing on Windows and sync with Raspberry Pi;
* IDE can't find the library or complete code;
* You don't have an Raspberry Pi yet, but you want to start your coding;
* You just want to use the utilities to simplify your code.

## Features

* Implements all methods and constants from RPi.GPIO;
* Supports RPiO;
* Code completion;
* Some useful utilities.

## Usages

### RPi.GPIO

#### Importing

Importing library
Python >= 2.7 & Python >= 3.2

```
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
	
    import FakeRPi.GPIO as GPIO
	
# Do your code here
```

Importing library
Python < 2.7 & Python < 3.4 OR Python >= 2.7 & Python >= 3.2 (Deprecated)

```
import imp
try:
    imp.find_module('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
	
    import FakeRPi.GPIO as GPIO
	
# Do your code here
```

#### Examples

```
import importlib.util
try: 
	# Check and import real RPi.GPIO library
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
	# If real RPi.GPIO library fails, load the fake one
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
	
    import FakeRPi.GPIO as GPIO

	

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

GPIO.output(18, GPIO.HIGH)

if GPIO.input(22):
    print("Pin 2 is HIGH")
else:
    print("Pin 2 is LOW")
	
GPIO.cleanup()
```

### RPi.Utilities

```
import importlib.util
try: 
	# Check and import real RPi.GPIO library
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
	# If real RPi.GPIO library fails, load the fake one
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
	
    import FakeRPi.GPIO as GPIO
	
import FakeRPi.Utilities

FakeRPi.Utilities.mode = FakeRPi.Utilities.PIN_TYPE_BOARD

pin1 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_1)
pin2 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_2)
pin3 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_3)
pin4 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_4)
pin5 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_5)
pin6 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_6)
pin7 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_7)
sda1 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_02_SDA1_I2C)

GPIO.setmode(RPiO.BOARD)
GPIO.setup(pin1, GPIO.OUTPUT)
GPIO.setup(pin1, GPIO.OUTPUT)
GPIO.setup(pin2, GPIO.INPUT)
GPIO.setup(pin3, GPIO.INPUT)
GPIO.setup(pin4, GPIO.OUTPUT)
GPIO.setup(pin5, GPIO.OUTPUT)
GPIO.setup(pin6, GPIO.INPUT)
GPIO.setup(pin7, GPIO.OUTPUT)

print(GPIO.input(pin6))
print(FakeRPi.Utilities.PIN_GPIO_GEN_6 == FakeRPi.Utilities.PIN_GPIO_25_GEN_6 == FakeRPi.Utilities.PIN_GPIO_25)  # Must be true
```