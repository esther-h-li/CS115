# === CS 115 Homework 4 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Esther Li
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 4 ===
from hw4_library import ppm_to_list_of_lists_of_rgbs, save_string_to_txt


def rgb_to_grayscale(image):
    """
    Mutates a 2D list of RGB pixels to a 2D list of grayscale values.
    Uses the CCIR 601 standard brightness formula:
        gray = int (0.299*red + 0.587*green + 0.114*blue)
    Does not return anything
    """
    def inList(lis):
        """For every tuple in a list, takes in a tuple of RGB values and returns the values of the corresponding brightness in a list"""
        return list(map(lambda tup: int((0.299*tup[0] + 0.587 * tup[1] + 0.144 * tup[2])) if int((0.299*tup[0] + 0.587 * tup[1] + 0.144 * tup[2])) < 255 else 255, lis))
    image[:] = list(map(inList, image))

def brightness_to_ascii(brightness):
    """
    Determines the ASCII character for each greyscale pixel depending on brightness
    @, #, %, *, =, +, -, :, and . are the ASCII characters used
    For every certain amount of brightness, it goes on to a less dense pixel
    """
    charas = "@#%*=+-:. "
    def map_(x):
        """
        Maps an individual pixel to an ASCII character
        """
        if(x>=231):
            return charas[9]
        elif x>= 205:
            return charas[8]
        elif x>= 180:
            return charas[7]
        elif x>= 154:
            return charas[6]
        elif x>= 128:
            return charas[5]
        elif x>=103:
            return charas[4]
        elif x>= 77:
            return charas[3]
        elif x>= 52:
            return charas[2]
        elif x>= 26:
            return charas[1]
        else:
            return charas[0]

    return map_(brightness)

def image_to_ascii_string(image):
    """
    Convert a 2D list of grayscale values (0–255)
    into a single string of ASCII characters where
    each row in the image corresponds to a line
    in the ASCII string. 

    Each line break is represented with \r\n
    to ensure compatibility with Windows 
    
    returns that string, only containing valid ASCII
    characters
    """
    def for2D(y):
        return "".join(list(map(lambda x: brightness_to_ascii(x), y)))
    return "\r\n".join(list(map(for2D,image))) 
    
def invert(image):
    """
    Inverts the brightness of the image
    """
    def _2DInvert(lis):
        """
        Inverts the brightness of a 2D list
        """
        return list(map(lambda x: 255-x if 255-x>0 else 0, lis))
    image[:] = list(map(_2DInvert, image))

def lighten(image):
    """
    Makes the image brighter by 30% with a max of 255
    """
    def _2Dbrightened(lis):
        """
        Makes a 2D list brighter by 30% with a max of 255
        """
        return list(map(lambda x: 1.3*x if 1.3*x<255 else 255, lis))
    image[:] = list(map(_2Dbrightened, image))


def darken(image):
    """
    Makes the image darker by 30% with a min of 0
    """
    def _2Ddarkened(lis):
        """
        Makes the 2D list darker by 30% with a min of 0
        """
        return list(map(lambda x: 0.7*x if 0.7*x>0 else 0, lis))
    image[:] = list(map(_2Ddarkened, image))




def erase(image):
    """
    Makes all pixels 0
    """
    def erase(lis):
        """
        Makes all elements in a 2D list 0
        """
        return list(map(lambda x: 0, lis))
    image[:] = list(map(erase, image))


def load_rgb_image(image_name):
    """
    Given a filename, image_name, returns 
    a grayscale image, 
    represented as a 2D list of intensities

    Do not change this function. It is just here for reference.
    """
    image = ppm_to_list_of_lists_of_rgbs(image_name)
    return image 


if __name__ == "__main__":
    # All code you want to run goes in this indented block
    # You can change the name of ppm_image_filename
    ppm_image_filename = "treasure_map.ppm"

    # This line calls our library function to load the image as 
    # a list of lists of rgb values
    image = load_rgb_image(ppm_image_filename)

    # Uncomment this line for Task 1
    # 
    rgb_to_grayscale(image)

    # Uncomment this line for Task 2
    # 
    ascii_string = image_to_ascii_string(image)

    # Uncomment this to save your ascii string to a text file
    # which can be read in other applications and uploaded
    # to Gradescope
    # 
    save_string_to_txt(ascii_string)
