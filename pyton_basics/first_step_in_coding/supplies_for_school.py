package_of_pencil_price = 5.8
package_of_marker_price = 7.2
cleaning_detergent_price = 1.2

number_of_pencil = int(input())
number_of_marker_package = int(input())
liters_of_cleaning_detergent = int(input())

discount = int(input())

price_sum = (number_of_pencil * package_of_pencil_price) + (number_of_marker_package * package_of_marker_price) \
            + (liters_of_cleaning_detergent * cleaning_detergent_price)
discount_price = price_sum - (price_sum*discount/100)

print(discount_price)

