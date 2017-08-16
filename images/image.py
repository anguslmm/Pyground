class Image:
    def __init__(self, file_path):
        file = open(file_path, 'rb')
        self.image_data = file.read()
        file.close()
        self.file_size = self.get_bytes_to_int(2, 4)
        self.pixel_data_offset = self.get_bytes_to_int(10, 4)
        self.header_size = self.get_bytes_to_int(14, 4)
        self.width = self.get_bytes_to_int(18, 4)
        self.height = self.get_bytes_to_int(22, 4)

        self.bits_per_pixel = self.get_bytes_to_int(28, 2)
        self.compression_type = self.get_bytes_to_int(30, 4)
        self.image_size_after_decompress = self.get_bytes_to_int(34, 4)
        self.preferred_x_res = self.get_bytes_to_int(38, 4)
        self.preferred_y_res = self.get_bytes_to_int(42, 4)
        self.clr_map_entry_count = self.get_bytes_to_int(46, 4)
        self.important_colors = self.get_bytes_to_int(50, 4)

        self.pixel_data = self.image_data_to_pixel_array()

        self.pixel_intensity = [[int(round(sum(pixel)/len(pixel))) for pixel in row] for row in self.pixel_data]

    def get_bytes_to_int(self, start: int, bytes: int) -> int:
        return sum([x * (256 ** i) for i, x in enumerate(self.image_data[start:start+bytes])])

    def image_data_to_pixel_array(self):
        row = -1
        pixels = []
        pixel_indices = range(self.pixel_data_offset, len(self.image_data), self.bits_per_pixel//8)
        for p, i in enumerate(reversed(pixel_indices)):
            if p%self.width == 0:
                if pixels:
                    pixels[row] = list(reversed(pixels[row]))
                pixels.append([])
                row += 1
            new_pixel = []
            for j in range(self.bits_per_pixel//8-1, -1, -1):
                new_pixel.append(self.get_bytes_to_int(i + j, 1))
            pixels[row].append(new_pixel)
        pixels[-1] = list(reversed(pixels[-1]))
        return pixels

    def __str__(self):
        result = ""
        breaks = {2, 6, 8, 10, 14, # File Header breaks
                  18, 22, 26, 28, 30, 34, 38, 42, 46, 50, 54 # Image Header breaks
                  }
        for i, c in enumerate(self.image_data):
            if i in breaks:
                result += '\n'
            result += "(" + str(c) + ")"

        return result


if __name__ == "__main__":
    i = Image('simple.bmp')

    print(i)
    print(i.file_size)
    print(i.pixel_data_offset)
    print(i.important_colors)
    print(i.image_size_after_decompress)
    print("****")
    print(i.pixel_data)
    print(i.pixel_intensity)