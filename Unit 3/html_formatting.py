from IPython.display import HTML, display

default_table_style    =  { "text-align" : "center",
                            "border"     : '4px solid black' } 

default_element_style  =  { "text-align" : "center",
                            "border"     : '1px solid black' } 

default_even_row_color =    "#ddffff" # Color specified by 6 hexadecimal digits
default_odd_row_color  =    "#ddffdd" # #RRGGBB


def make_html_table_from_datalist( datalist, 
                                   table_style    = default_table_style, 
                                   element_style  = default_element_style,
                                   even_row_color = default_even_row_color,
                                   odd_row_color  = default_odd_row_color  ):
    
    table_style_str = make_html_style_string_from_dictionary( table_style )
    html_string = "<table {}>\n".format(table_style_str)
    
    elt_style_str   = make_html_style_string_from_dictionary( element_style )
    
    even_row = True        # store whether row is even
    for row in datalist:
        row_col = even_row_color if even_row else odd_row_color
        even_row = not even_row # toggle even_row variable
        
        # start table row:
        html_string += '<tr style="background-color:{}">\n'.format(row_col) 
        for element in row:
            html_string += "<td {}>{}</td> ".format(elt_style_str, str(element)) 
        html_string += "\n</tr>\n" # end table row
    return html_string


def make_html_style_string_from_dictionary( style_dict ):
    style_str = ""
    if style_dict:
        style_str = 'style="'
        for style in style_dict: 
            style_str += "{}:{};".format(style, style_dict[style])
        style_str += '"' # add final close quote
    return style_str


def display_datalist_as_html_table( datalist ):
     html_table = make_html_table_from_datalist( datalist )
     display(HTML("<center>" + html_table + "</center>"))
