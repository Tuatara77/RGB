from math import sin, cos, radians, sqrt

class RGB:
    """A general class for handling RGB values"""
    def __init__(self, r: int, g: int, b: int):
        assert type(r) == type(g) == type(b) == int, "RGB values must be integers"
        self.r = self._check(r)
        self.g = self._check(g)
        self.b = self._check(b)
    
    def getcolour(self) -> tuple: 
        """Returns a tuple of the RGB values"""
        return (self.r, self.g, self.b)

    def setcolour(self, new_r: int, new_g: int, new_b: int) -> None:
        assert type(new_r) == type(new_g) == type(new_b) == int, "RGB values must be integers"
        self.r = self._check(new_r)
        self.g = self._check(new_g)
        self.b = self._check(new_b)

    def convert_hex(self) -> str:
        """Returns the hex conversion of the current decimal RGB value"""
        hex_r = hex(self.r)[2:]
        hex_g = hex(self.g)[2:]
        hex_b = hex(self.b)[2:]
        if len(hex_r) == 1: hex_r = f"0{hex_r}"
        if len(hex_g) == 1: hex_g = f"0{hex_g}"
        if len(hex_b) == 1: hex_b = f"0{hex_b}"
        
        return f"#{hex_r}{hex_g}{hex_b}"

    def _check(self, n) -> int:
        if n < 0: return 0
        elif n > 255: return 255
        return n
    
    def linear_shift(self, changerate: int=3, minbrightness: int=0, maxbrightness: int=255) -> None:
        """Shifts the current RGB value around by a variable changerate between two decimal values"""
        if                   self.r <  maxbrightness and                 self.g == minbrightness and                 self.b == maxbrightness: self.r += changerate
        elif minbrightness < self.r <= maxbrightness and                 self.g == maxbrightness and                 self.b == minbrightness: self.r -= changerate
        elif                 self.r == maxbrightness and                 self.g <  maxbrightness and                 self.b == minbrightness: self.g += changerate
        elif                 self.r == minbrightness and minbrightness < self.g <= maxbrightness and                 self.b == maxbrightness: self.g -= changerate
        elif                 self.r == minbrightness and                 self.g == maxbrightness and                 self.b <  maxbrightness: self.b += changerate
        elif                 self.r == maxbrightness and                 self.g == minbrightness and minbrightness < self.b <= maxbrightness: self.b -= changerate

        if self.r <= minbrightness: self.r = minbrightness
        if self.r >= maxbrightness: self.r = maxbrightness
        if self.g <= minbrightness: self.g = minbrightness
        if self.g >= maxbrightness: self.g = maxbrightness
        if self.b <= minbrightness: self.b = minbrightness
        if self.b >= maxbrightness: self.b = maxbrightness


class RGBRotate(RGB):
    """
    A class that piggybacks off of the RGB class that shifts 
    the RGB value via a trigonometric matrix

    Stolen and adapted from stackoverflow: https://stackoverflow.com/a/8510751"""
    def __init__(self, r: int, g: int, b: int): 
        super().__init__(r,g,b)
        self.matrix = [[1,0,0],[0,1,0],[0,0,1]]

    def _clamp(self, n):
        if n < 0: return 0
        elif n > 255: return 255
        return int(n+0.5)

    def set_hue_rotation(self, degrees: float) -> None:
        """Sets the rate of change of the RGB value"""
        cosA = cos(radians(degrees))
        sinA = sin(radians(degrees))
        self.matrix[0][0] = cosA + (1.0 - cosA) / 3.0
        self.matrix[0][1] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
        self.matrix[0][2] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
        self.matrix[1][0] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
        self.matrix[1][1] = cosA + 1./3.*(1.0 - cosA)
        self.matrix[1][2] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
        self.matrix[2][0] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
        self.matrix[2][1] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
        self.matrix[2][2] = cosA + 1./3. * (1.0 - cosA)

    def rotate(self) -> None:
        """Rotates the RGB value by a matrix defined by set_hue_rotation()"""
        self.r = self._clamp(self.r * self.matrix[0][0] + self.g * self.matrix[0][1] + self.b * self.matrix[0][2])
        self.g = self._clamp(self.r * self.matrix[1][0] + self.g * self.matrix[1][1] + self.b * self.matrix[1][2])
        self.b = self._clamp(self.r * self.matrix[2][0] + self.g * self.matrix[2][1] + self.b * self.matrix[2][2])