import math
import json

def row_generator(books, offset, maximum_image_width):
    """
    This function generates a row of books
    """
    markdown = ""
    for c in range(len(books)):
        markdown += "| [" + str(offset+c+1) + ". "+ books[c]['title'] + "]" + "(" + books[int(c)]['URL'] + ")"
    markdown += "|\n" + len(books)*("|:" + 3 * "-" + ":")+"|" + '\n'
    for c in range(len(books)):
        markdown += "| **By:** " + books[c]['author'] + " <br>" + "**Year:** " +  books[c]['year']
        if books[c]['publisher']:
            markdown += " <br>" + "**Publisher:** " + books[c]['publisher']
        if books[c]['edition']:
            markdown += " <br>" + "**Edition:** " + books[c]['edition']
    markdown += "|\n"
    for c in range(len(books)):
        if books[c]['front_page']:
            markdown += "|  <img src=\"" + books[c]['front_page'] +"\" alt=\""+\
            books[c]['title'] + "\" width = \"" +str(maximum_image_width) + "px\" />"
        else:
            markdown += "| Front Cover Thumbnail Not Found!"
    markdown += "|\n\n"
    return markdown
    
def book_grid_generator(grid_size, json_file, maximum_image_width)->None:
    with open(json_file) as f:
        books = json.load(f)
    
    sorted_books = sorted(books['books'], key = lambda x: x['year'], reverse=True)
    rows = math.floor(len(sorted_books)/grid_size)
    markdown = ""
    for i in range(0, len(sorted_books),grid_size):
        markdown += row_generator(sorted_books[i:min(i + grid_size,len(sorted_books))],i, maximum_image_width)
#     print(markdown)
    with open("Books.md",'w') as f:
        f.write(markdown)
        
if __name__ == '__main__':
    book_grid_generator(3,'Books.json', 400)
