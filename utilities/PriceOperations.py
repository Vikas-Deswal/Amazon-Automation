import re


class PriceOperations:
    def extract_price(self, output):
        """
        Extracts the price from the given output string.

        Args:
        output: The input string containing the price.

        Returns:
        The extracted price as an integer, or None if no price is found.
        """
        # Remove currency symbol and commas
        price_str = output.replace("₹", "").replace(",", "")

        # Extract the price using regular expression
        match = re.search(r"(\d+\.\d+)", price_str)

        if match:
            price_float = float(match.group(1))
            return price_float
        else:
            return None
