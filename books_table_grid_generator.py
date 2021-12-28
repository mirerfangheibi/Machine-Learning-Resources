import math
import json

def row_generator(books, offset, maximum_image_width):
    
    markdown = ""
    for c in range(len(books)):
        markdown += "| [" + str(offset+c+1) + ". "+ books[int(c)]['title'] + "]" +\
        "(" + books[int(c)]['URL'] + ")"
    markdown += "|"
    markdown += '\n' + len(books)*("|:" + 3 * "-" + ":")+"|" + '\n'
    for c in range(len(books)):
        markdown += "| **By:** " + books[int(c)]['author'] + \
        " <br>" + "**Year:** " +  books[int(c)]['year']
        if books[int(c)]['publisher']:
            markdown += " <br>" + "**Publisher:** " + books[int(c)]['publisher']
        if books[int(c)]['edition']:
            markdown += " <br>" + "**Edition:** " + books[int(c)]['edition']
    markdown += "|\n"
    for c in range(len(books)):
        if books[int(c)]['front_page']:
            markdown += "|  <img src=\"" + books[int(c)]['front_page'] +"\" alt=\""+\
            books[int(c)]['title'] + "\" width = \"" +str(maximum_image_width) + "px\" />"
        else:
            markdown += "| Front Cover Thumbnail Not Found!"
        markdown += "|\n"
        
        return markdown
    
def book_grid_generator(grid_size, json_file, maximum_image_width)->None:
    with open(json_file) as f:
        books = json.load(f)
    
    sorted_books = sorted(books['books'], key = lambda x: x['year'], reverse=True)
    rows = math.floor(len(sorted_books)/grid_size)
    markdown = ""
    i=0
    for r in range(rows):
        markdown += row_generator(sorted_books[i:i + grid_size],i, maximum_image_width)
        markdown += 3*'\n'
        i += grid_size
    if i<len(sorted_books):
        remaining = len(sorted_books)-i
        markdown += row_generator(sorted_books[i:i + remaining],i, maximum_image_width)
        markdown += 3*'\n'
    
    print(markdown)
