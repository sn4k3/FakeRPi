__author__ = 'Tiago'

"""
Board pin constants
Pi B REV 2 & B+ J8
"""
#PIN_3v = 1                             # DC Power 3.3v
#PIN_5v = 2                             # DC Power 5v

PIN_GPIO_02 = 3                         # GPIO02 (SDA1, I2C)
PIN_GPIO_02_SDA1_I2C = PIN_GPIO_02      # GPIO02 (SDA1, I2C)
#PIN_5v = 4                             # DC Power 5v

PIN_GPIO_03 = 5                         # GPIO03 (SCL1, I2C)
PIN_GPIO_03_SCL1_I2C = PIN_GPIO_03      # GPIO03 (SCL1, I2C)
#PIN_GROUND = 6                         # Ground

PIN_GPIO_04 = 7                         # GPIO04 (GPIO_GCLK)
PIN_GPIO_04_GCLK = PIN_GPIO_04          # GPIO04 (GPIO_GCLK)
PIN_GPIO_14 = 8                         # GPIO14 (TXD0) - UART
PIN_GPIO_14_TXD0 = PIN_GPIO_14          # GPIO14 (TXD0) - UART

#PIN_GROUND = 9                         # Ground
PIN_GPIO_15 = 10                        # GPIO15 (RXD0) - UART
PIN_GPIO_15_RXD0 = PIN_GPIO_15          # GPIO15 (RXD0) - UART

PIN_GPIO_17 = 11                        # GPIO17 (GEN0)
PIN_GPIO_17_GEN_0 = PIN_GPIO_17         # GPIO17 (GEN0)
PIN_GPIO_GEN_0 = PIN_GPIO_17            # GPIO17 (GEN0)
PIN_GPIO_18 = 12                        # GPIO18 (GEN1)
PIN_GPIO_18_GEN_1 = PIN_GPIO_18         # GPIO18 (GEN1)
PIN_GPIO_GEN_1 = PIN_GPIO_18            # GPIO18 (GEN1)

PIN_GPIO_27 = 13                        # GPIO27 (GEN2)
PIN_GPIO_27_GEN_2 = PIN_GPIO_27         # GPIO27 (GEN2)
PIN_GPIO_GEN_2 = PIN_GPIO_27            # GPIO27 (GEN2)
#PIN_GROUND = 14                        # Ground

PIN_GPIO_22 = 15                        # GPIO22 (GEN3)
PIN_GPIO_22_GEN_3 = PIN_GPIO_22         # GPIO22 (GEN3)
PIN_GPIO_GEN_3 = PIN_GPIO_22            # GPIO22 (GEN3)
PIN_GPIO_23 = 16                        # GPIO23 (GEN4)
PIN_GPIO_23_GEN_4 = PIN_GPIO_23         # GPIO23 (GEN4)
PIN_GPIO_GEN_4 = PIN_GPIO_23            # GPIO23 (GEN4)

#PIN_3v = 17                            # DC Power 3.3v
PIN_GPIO_24 = 18                        # GPIO24 (GEN5)
PIN_GPIO_24_GEN_5 = PIN_GPIO_24         # GPIO24 (GEN5)
PIN_GPIO_GEN_5 = PIN_GPIO_24            # GPIO24 (GEN5)

PIN_GPIO_10 = 19                        # GPIO10 (SPI_MOSI)
PIN_GPIO_10_SPI_MOSI = PIN_GPIO_10      # GPIO10 (SPI_MOSI)
#PIN_GROUND = 20                        # Ground

PIN_GPIO_09 = 21                        # GPIO09 (SPI_MISO)
PIN_GPIO_09_SPI_MISO = PIN_GPIO_09      # GPIO09 (SPI_MISO)
PIN_GPIO_25 = 22                        # GPIO25 (GEN6)
PIN_GPIO_25_GEN_6 = PIN_GPIO_25         # GPIO25 (GEN6)
PIN_GPIO_GEN_6 = PIN_GPIO_25            # GPIO25 (GEN6)

PIN_GPIO_11 = 23                        # GPIO11 (SPI_CLK)
PIN_GPIO_11_SPI_CLK = PIN_GPIO_11       # GPIO11 (SPI_CLK)
PIN_GPIO_08 = 24                        # GPIO08 (SPI_CE0_N)
PIN_GPIO_08_SPI_CE0_N = PIN_GPIO_08     # GPIO08 (SPI_CE0_N)

#PIN_GROUND = 25                        # Ground
PIN_GPIO_07 = 26                        # GPIO07 (SPI_CE0_N)
PIN_GPIO_07_SPI_CE1_N = PIN_GPIO_07     # GPIO07 (SPI_CE1_N)

PIN_ID_SD = 27                          # I2C ID EEPROM
PIN_ID_SD_I2C_ID_EEPROM = PIN_ID_SD     # I2C ID EEPROM
PIN_ID_SC = 28                          # I2C ID EEPROM
PIN_ID_SC_I2C_ID_EEPROM = PIN_ID_SC     # I2C ID EEPROM

PIN_GPIO_05 = 29                        # GPIO05 (GEN7)
PIN_GPIO_05_GEN_7 = PIN_GPIO_05         # GPIO05 (GEN7)
PIN_GPIO_GEN_7 = PIN_GPIO_05            # GPIO05 (GEN7)
#PIN_GROUND = 30                        # Ground

PIN_GPIO_06 = 31                        # GPIO06 (GEN8)
PIN_GPIO_06_GEN_8 = PIN_GPIO_06         # GPIO06 (GEN8)
PIN_GPIO_GEN_8 = PIN_GPIO_06            # GPIO06 (GEN8)
PIN_GPIO_12 = 32                        # GPIO12 (GEN9)
PIN_GPIO_12_GEN_9 = PIN_GPIO_12         # GPIO12 (GEN9)
PIN_GPIO_GEN_9 = PIN_GPIO_12            # GPIO12 (GEN9)

PIN_GPIO_13 = 33                        # GPIO13 (GEN10)
PIN_GPIO_13_GEN_10 = PIN_GPIO_13        # GPIO13 (GEN10)
PIN_GPIO_GEN_10 = PIN_GPIO_13           # GPIO13 (GEN10)
#PIN_GROUND = 34                        # Ground

PIN_GPIO_19 = 35                        # GPIO19 (GEN11)
PIN_GPIO_19_GEN_11 = PIN_GPIO_19        # GPIO19 (GEN11)
PIN_GPIO_GEN_11 = PIN_GPIO_19           # GPIO19 (GEN11)
PIN_GPIO_16 = 36                        # GPIO16 (GEN12)
PIN_GPIO_16_GEN_12 = PIN_GPIO_16        # GPIO16 (GEN12)
PIN_GPIO_GEN_12 = PIN_GPIO_16           # GPIO16 (GEN12)

PIN_GPIO_26 = 37                        # GPIO26 (GEN13)
PIN_GPIO_26_GEN_13 = PIN_GPIO_26        # GPIO26 (GEN13)
PIN_GPIO_GEN_13 = PIN_GPIO_26           # GPIO26 (GEN13)
PIN_GPIO_20 = 38                        # GPIO20 (GEN14)
PIN_GPIO_20_GEN_14 = PIN_GPIO_20        # GPIO20 (GEN14)
PIN_GPIO_GEN_14 = PIN_GPIO_20           # GPIO13 (GEN14)

#PIN_GROUND = 39                        # Ground
PIN_GPIO_21 = 40                        # GPIO21 (GEN15)
PIN_GPIO_21_GEN_15 = PIN_GPIO_21        # GPIO21 (GEN15)
PIN_GPIO_GEN_15 = PIN_GPIO_21           # GPIO21 (GEN15)

PIN_TYPE_BOARD = 'BOARD'
PIN_TYPE_BCM = 'BCM'

PINS = {
    PIN_TYPE_BOARD: {
        PIN_GPIO_02: PIN_GPIO_02,
        PIN_GPIO_03: PIN_GPIO_03,
        PIN_GPIO_04: PIN_GPIO_04,
        PIN_GPIO_14: PIN_GPIO_14,
        PIN_GPIO_15: PIN_GPIO_15,
        PIN_GPIO_17: PIN_GPIO_17,
        PIN_GPIO_18: PIN_GPIO_18,
        PIN_GPIO_27: PIN_GPIO_27,
        PIN_GPIO_22: PIN_GPIO_22,
        PIN_GPIO_23: PIN_GPIO_23,
        PIN_GPIO_24: PIN_GPIO_24,
        PIN_GPIO_10: PIN_GPIO_10,
        PIN_GPIO_09: PIN_GPIO_09,
        PIN_GPIO_25: PIN_GPIO_25,
        PIN_GPIO_11: PIN_GPIO_11,
        PIN_GPIO_08: PIN_GPIO_08,
        PIN_GPIO_07: PIN_GPIO_07,
        #PIN_ID_SD: PIN_ID_SD,
        #PIN_ID_SC: PIN_ID_SC,
        PIN_GPIO_05: PIN_GPIO_05,
        PIN_GPIO_06: PIN_GPIO_06,
        PIN_GPIO_12: PIN_GPIO_12,
        PIN_GPIO_13: PIN_GPIO_13,
        PIN_GPIO_19: PIN_GPIO_19,
        PIN_GPIO_16: PIN_GPIO_16,
        PIN_GPIO_26: PIN_GPIO_26,
        PIN_GPIO_20: PIN_GPIO_20,
        PIN_GPIO_21: PIN_GPIO_21
    },
    PIN_TYPE_BCM: {
        PIN_GPIO_02: 2,
        PIN_GPIO_03: 3,
        PIN_GPIO_04: 4,
        PIN_GPIO_14: 14,
        PIN_GPIO_15: 15,
        PIN_GPIO_17: 17,
        PIN_GPIO_18: 18,
        PIN_GPIO_27: 27,
        PIN_GPIO_22: 22,
        PIN_GPIO_23: 23,
        PIN_GPIO_24: 24,
        PIN_GPIO_10: 10,
        PIN_GPIO_09: 9,
        PIN_GPIO_25: 25,
        PIN_GPIO_11: 11,
        PIN_GPIO_08: 8,
        PIN_GPIO_07: 7,
        #PIN_ID_SD: PIN_ID_SD,
        #PIN_ID_SC: PIN_ID_SD,
        PIN_GPIO_05: 5,
        PIN_GPIO_06: 6,
        PIN_GPIO_12: 12,
        PIN_GPIO_13: 13,
        PIN_GPIO_19: 19,
        PIN_GPIO_16: 16,
        PIN_GPIO_26: 26,
        PIN_GPIO_20: 20,
        PIN_GPIO_21: 21
    }
}


mode = PIN_TYPE_BOARD


def setmode(type):
    """
    Set the default pin board type to use with get_pin function
    :param type:
    :return:
    """
    mode = type


def get_pin(pin, board_type=mode):
    """
    Get the appropriate pin number
    :param pin: Pin to use. eg: PIN_GPIO_02
    :param board_type: Pin type (BCM or BOARD)
    :return:
    """
    return PINS[board_type][pin]