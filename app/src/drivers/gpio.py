class GpioOutputDriver:
    def __init__(self, pin_number: int) -> None:
        self._pin_number = pin_number
        self._state = None

    @property
    def state(self) -> bool:
        # code to read pin state or just return internal variable self._state
        return self._state

    @state.setter
    def state(self, val: bool):
        # code to set pin state
        self._state = val


if __name__ == "__main__":
    relays_controller = GpioOutputDriver(pin_number=2)
    relays_controller.relay_0_status
