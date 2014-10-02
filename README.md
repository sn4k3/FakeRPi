FakeRPI
=======

Develop for Raspberry Pi on Windows or other systems that don't have RPI.GPIO libraries.

It implements RPI.GPIO functions and return None values.

When we are developing on some IDE's, they will verify the code syntax and consequently report many errors as the library is not present on include paths. That can be annoying for the user, as they see a lot of errors everywhere and some red lines. With FakeRPI you can fix that and also benefits from code completion and some utilities.

This is not an emulator of Rasberry Pi!

## When to use

* Developing on Windows and sync with Raspberry Pi;
* IDE can't find the library or complete code;
* You don't have an Raspberry Pi yet, but you want to start your coding;
* You just want to use the utilities to simplify your code.

## Features

* Implements all methods and constants from RPI.GPIO;
* Supports RPIO;
* Code completion;
* Some useful utilities.

## Usages

### RPI.GPIO

#### Importing

Importing library
Python >= 2.7 & Python >= 3.1

```
import importlib.util
try:
    importlib.util.find_spec('RPI.GPIO')
    import RPI.GPIO as GPIO
except ImportError:
    """
    import FakeRPI.GPIO as GPIO
    OR
    import FakeRPI.RPIO as RPIO
    """
	
    import FakeRPI.GPIO as GPIO
	
# Do your code here
```

Importing library
Python < 2.7 & Python < 3.4 OR Python >= 2.7 & Python >= 3.1 (Deprecated)

```
import imp
try:
    imp.find_module('RPI.GPIO')
    import RPI.GPIO as GPIO
except ImportError:
    """
    import FakeRPI.GPIO as GPIO
    OR
    import FakeRPI.RPIO as RPIO
    """
	
    import FakeRPI.GPIO as GPIO
	
# Do your code here
```

#### Examples

```
import importlib.util
try: 
	# Check and import real RPI.GPIO library
    importlib.util.find_spec('RPI.GPIO')
    import RPI.GPIO as GPIO
except ImportError:
	# If real RPI.GPIO library fails, load the fake one
    """
    import FakeRPI.GPIO as GPIO
    OR
    import FakeRPI.RPIO as RPIO
    """
	
    import FakeRPI.GPIO as GPIO

	

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

### RPI.Utilities

```
import importlib.util
try: 
	# Check and import real RPI.GPIO library
    importlib.util.find_spec('RPI.GPIO')
    import RPI.GPIO as GPIO
except ImportError:
	# If real RPI.GPIO library fails, load the fake one
    """
    import FakeRPI.GPIO as GPIO
    OR
    import FakeRPI.RPIO as RPIO
    """
	
    import FakeRPI.GPIO as GPIO
	
import FakeRPI.Utilities as Utilities

Utilities.set_default_pintype(Utilities.PIN_TYPE_BOARD)

pin1 = Utilities.get_pin(Utilities.PIN_GPIO_GEN_1)
pin2 = Utilities.get_pin(Utilities.PIN_GPIO_GEN_2)
pin3 = Utilities.get_pin(Utilities.PIN_GPIO_GEN_3)
pin4 = Utilities.get_pin(Utilities.PIN_GPIO_GEN_4)
pin5 = Utilities.get_pin(Utilities.PIN_GPIO_GEN_5)
pin6 = Utilities.get_pin(Utilities.PIN_GPIO_GEN_6)
pin7 = Utilities.get_pin(Utilities.PIN_GPIO_GEN_7)
sda1 = Utilities.get_pin(Utilities.PIN_GPIO_02_SDA1_I2C)

GPIO.setmode(RPIO.BOARD)
GPIO.setup(pin1, GPIO.OUTPUT)
GPIO.setup(pin1, GPIO.OUTPUT)
GPIO.setup(pin2, GPIO.INPUT)
GPIO.setup(pin3, GPIO.INPUT)
GPIO.setup(pin4, GPIO.OUTPUT)
GPIO.setup(pin5, GPIO.OUTPUT)
GPIO.setup(pin6, GPIO.INPUT)
GPIO.setup(pin7, GPIO.OUTPUT)

print(GPIO.input(pin6))
print(Utilities.PIN_GPIO_GEN_6 == Utilities.PIN_GPIO_25_GEN_6 == Utilities.PIN_GPIO_25)  # Must be true
```