# Algorithm: Array of products
#
# Function that takes in a non-empty array of integers and returns an array of the same length, where each
# element in the output array is equal to the product of every other number in the input array.


# Define function
def array_of_products(array):
    # Create an array of the same length that has all values of 1.
    products = [1 for _ in range(len(array))]

    # Iterate through the array with first pointer.
    for i in range(len(array)):
        running_product = 1
        # Second pointer
        for j in range(len(array)):
            # Conditional statement to only use the product of every other number in the array.
            if i != j:
                # Multiply each of these values by our running product
                running_product *= array[j]
        # Update values in the array
        products[i] = running_product

    return


print(array_of_products([1, 2, 3, 4, 5, 6, 7]))
