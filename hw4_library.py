def ppm_to_list_of_lists_of_rgbs(filename):
    """
    Given a filename of a plaintext PPM P3 file,
    returns a (M x N x 3) list
    of M rows, each of which contain N tuples of 3 values, which 
    correspond to the R,G and B values for each pixel. 
    """
    with open(filename, 'r') as f:
        def next_line():
            line = f.readline()
            while line.startswith('#'):
                line = f.readline()
            return line

        ppm_format = next_line().strip()
        if ppm_format != 'P3':
            raise ValueError("Only ASCII PPM (P3) format supported")

        width, height = map(int, next_line().split())
        max_val = int(next_line().strip())
        if max_val != 255:
            raise ValueError("Only pixel values from 0 to 255 supported")

        pixel_data = [int(x) for x in f.read().split()]
        pixels = [(pixel_data[i], pixel_data[i+1], pixel_data[i+2])
                  for i in range(0, len(pixel_data), 3)]

        return [pixels[i*width:(i+1)*width] for i in range(height)]


def save_string_to_txt(ascii_string, filename = "treasure_map.txt"):
    with open(filename, "w", encoding="ascii", newline="\r\n") as f:
        f.write(ascii_string)
        if not ascii_string.endswith(("\n", "\r")):
            f.write("\r\n")
    print(f"Saved ascii_string to file: {filename}")


