__author__ = 'Tiago'
__documentation__ = 'https://pythonhosted.org/RPIO/rpio_py.html#ref-rpio-py-additions'

from FakeRPi.GPIO import *


RPI_REVISION = 1
RPI_REVISION_HEX = 0x0002


def gpio_function(channel):
    """
    returns the current setup of a gpio (IN, OUT, ALT0)
    :param channel:
    :return:
    """
    return IN


def set_pullupdn(channel, pud):
    """
    set a pullup or -down resistor on a GPIO
    :param channel:
    :param pud:
    :return:
    """
    pass


def forceinput(channel):
    """
    Reads the value of any gpio without needing to call setup() first
    :param channel:
    :return:
    """
    pass


def forceoutput(channel, value):
    """
    Writes a value to any gpio without needing to call setup() first (warning: this can potentially harm your Raspberry)
    :param channel:
    :param value:
    :return:
    """
    pass


def sysinfo():
    """
    returns (hex_rev, model, revision, mb-ram and maker) of this Raspberry
    :return:
    """
    return (RPI_REVISION_HEX, 'B+', RPI_REVISION, '512', 'RaspberryPi')


def version():
    """
    (version_rpio, version_cgpio)
    :return:
    """
    return (RPI_REVISION, VERSION)


def add_interrupt_callback(channel, callback, edge='both', pull_up_down=PUD_DOWN, threaded_callback=False,
                           debounce_timeout_ms=None):
    """
    Interrupts are used to receive notifications from the kernel when GPIO state changes occur.
    Advantages include minimized cpu consumption, very fast notification times, and the ability to trigger on specific edge transitions (rising, falling or both).
    You can also set a software pull-up or pull-down resistor.
    :param channel:
    :param callback:
    :param edge: Possible edges are rising, falling and both (default).
    :param pull_up_down: Possible pull_up_down values are RPIO.PUD_UP, RPIO.PUD_DOWN and RPIO.PUD_OFF (default).
    :param threaded_callback: If threaded_callback is True, the callback will be started inside a thread.
    Else the callback will block RPIO from waiting for interrupts until it has finished (in the meantime no further callbacks are dispatched).
    :param debounce_timeout_ms: If debounce_timeout_ms is set, interrupt callbacks will not be started until the specified milliseconds have passed since the last interrupt. Adjust this to your needs (typically between 10ms and 100ms).
    :return:
    """
    pass


def add_tcp_callback(port, callback, threaded_callback=False):
    """
    Adds a socket server callback, which will be started when a connected socket client sends something.
    This is implemented by RPIO creating a TCP server socket at the specified port.
    Incoming connections will be accepted when RPIO.wait_for_interrupts() runs.
    The callback must accept exactly two parameters: socket and message (eg. def callback(socket, msg)).
    :param port:
    :param callback:
    :param threaded_callback:
    :return:
    """
    pass


def del_interrupt_callback(channel):
    pass


def close_tcp_client(fileno):
    pass


def wait_for_interrupts(threaded=False, epoll_timeout=1):
    """
    This is the main blocking loop which, while active, will listen for interrupts and start your custom callbacks.
    At some point in your script you need to start this to receive interrupt callbacks.
    This blocking method is perfectly suited as “the endless loop that keeps your script running”.
    :param threaded: With the argument threaded=True, this method starts in the background while your script continues in the main thread (RPIO will automatically shut down the thread when your script exits)
    :param epoll_timeout:
    :return:
    """
    pass


def stop_waiting_for_interrupts():
    pass