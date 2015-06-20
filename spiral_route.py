
eol = '\n'
def collapse_matrix(matrix):
    collapsed_matrix = eol.join(matrix)
    return collapsed_matrix

def collate_matrix(matrix):
    collated_matrix = []
    max_rows = len(matrix) - 1
    for row in range(max_rows):
        collated_matrix.append(''.join(matrix[row]))
    return collated_matrix

def shift_text(text, offset):
    new_text = text[offset:] + text[0:offset]
    return new_text

def sort_list(list, order="forward"):
    sorted_list = list
    if order == "forward":
        sorted_list = sorted(list)
    else:
        list.reverse()
        sorted_list = list
    return sorted_list

def populate_spiral_row(snippet, row, column_list, matrix):
    position = 0
    #print(snippet, row, column_list)
    for column in column_list:
        matrix[row][column] = snippet[position]
        position = position + 1
    return matrix 

def populate_spiral_column(snippet, row_list, column, matrix):
    position = 0
    for row in row_list:
        matrix[row][column] = snippet[position]
        position = position + 1
    return matrix

def populate_matrix(text, rows, columns, direction="reading"):
    pass

def spiral_route_cipher(original_text, rows, columns, direction = "counter-clockwise"):
    text = original_text
    rows_list = range(rows)
    columns_list = range(columns)
    text_cursor = 0
    partial_matrix = [[' ' for x in range(columns)] for x in range(rows)]
    if direction == "counter-clockwise":
        while len(text) > text_cursor:
            left = text[text_cursor:text_cursor + len(rows_list)] 
            rows_list = sort_list(rows_list, "forward")
            columns_list = sort_list(columns_list, "forward")
            if len(columns_list) > 0:
                column = columns_list.pop(0)
            text_cursor = text_cursor + len(rows_list)
            #print(left, rows_list, column)
            partial_matrix = populate_spiral_column(left, rows_list, column, partial_matrix)
            if len(text) > text_cursor:
                bottom = text[text_cursor:text_cursor + len(columns_list)]
                rows_list = sort_list(rows_list, "reversed")
                columns_list = sort_list(columns_list, "forward")
                if len(rows_list) > 0:
                    row = rows_list.pop(0)
                text_cursor = text_cursor + len(columns_list)    
                #print(bottom, row, columns_list)
                partial_matrix = populate_spiral_row(bottom, row, columns_list, partial_matrix)
                if len(text) > text_cursor:
                    right = text[text_cursor:text_cursor + len(rows_list)][::-1]
                    rows_list = sort_list(rows_list, "reversed")
                    columns_list = sort_list(columns_list, "reversed")
                    if len(columns_list) > 0:
                        column = columns_list.pop(0)
                    text_cursor = text_cursor + len(rows_list)
                    #print(right, rows_list, column)
                    partial_matrix = populate_spiral_column(right, rows_list, column, partial_matrix)
                    if len(text) > text_cursor:
                        top = text[text_cursor:text_cursor + len(columns_list)][::-1]
                        rows_list = sort_list(rows_list, "reversed")
                        columns_list = sort_list(columns_list, "reversed")
                        if len(rows_list) > 0:
                            row = rows_list.pop(-1)
                        text_cursor = text_cursor + len(columns_list)
                        #print(top, row, columns_list)
                        partial_matrix = populate_spiral_row(top, row, columns_list, partial_matrix)
        return partial_matrix 

def main():
    text = '?OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR'
    rows = 7
    columns = 14
    for offset in range(0, len(text)):
        shifted_text = shift_text(text, offset)
        #new_matrix = ['' for x in range(rows)]
        new_matrix = spiral_route_cipher(shifted_text, rows, columns, direction = "counter-clockwise") 
        matrix_collated_columns = collate_matrix(new_matrix)
        matrix_collated_text = collapse_matrix(matrix_collated_columns)
        print matrix_collated_text, eol

if __name__ == "__main__":
    main()
