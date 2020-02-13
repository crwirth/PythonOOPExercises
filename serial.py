"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate_number()
    100

    >>> serial.generate_number()
    101

    >>> serial.generate_number()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Create new number generator starting at start"""
        self.start = self.next = start
    
    def __repr__(self):
        """Show the representation"""
        return f"SerialGenerator start={self.start} next={self.next}"

    def generate_number(self):
        """Returns next serial number"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Resets number back to originial value of start"""
        self.next = self.start



