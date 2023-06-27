# # how to crop image
# from PIL import Image

# def crop_image(image_path, coordinates, output_path):
#     """
#     Crop the image at the specified coordinates and save it to the output path.
    
#     Parameters:
#         image_path (str): The path to the input image.
#         coordinates (tuple): The coordinates (left, upper, right, lower) of the area to crop.
#         output_path (str): The path to save the cropped image.
#     """
#     # Open the image
#     image = Image.open(image_path)

#     # Crop the image
#     cropped_image = image.crop(coordinates)

#     # Save the cropped image
#     cropped_image.save(output_path)


# # Usage example
# input_image_path = "path/to/input/image.jpg"
# output_image_path = "path/to/output/cropped_image.jpg"
# crop_coordinates = (100, 100, 400, 400)  # Example coordinates (left, upper, right, lower)

# crop_image(input_image_path, crop_coordinates, output_image_path)


