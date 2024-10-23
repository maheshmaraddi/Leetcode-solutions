def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # Create a list of strings for each row
    rows = [''] * numRows
    current_row = 0
    direction = -1  # to alternate between moving up and down

    # Traverse through the characters in the string
    for char in s:
        rows[current_row] += char
        # Change direction when hitting the top or bottom row
        if current_row == 0 or current_row == numRows - 1:
            direction *= -1
        current_row += direction

    # Join all the rows to get the final zigzag pattern
    return ''.join(rows)