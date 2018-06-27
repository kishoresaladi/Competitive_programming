def intersection(point1, length1, point2, length2):
   
    start = max(point1, point2)
    end = min(point1 + length1, point2 + length2)

    
    if start >= end:
        return (None, None)

    
    intersecting_length = end - start

    return (start,intersecting_length)


def find_rectangular_overlap(rect1, rect2):
    
    x_cord, overlap_width  = intersection(rect1['left_x'],
                                                         rect1['width'],
                                                         rect2['left_x'],
                                                         rect2['width'])
    y_cord, overlap_height = intersection(rect1['bottom_y'],
                                                         rect1['height'],
                                                         rect2['bottom_y'],
                                                         rect2['height'])

   
    if not overlap_width or not overlap_height:
        return {
            'left_x'   : None,
            'bottom_y' : None,
            'width'    : None,
            'height'   : None,
        }

    return {
        'left_x'   : x_cord,
        'bottom_y' : y_cord,
        'width'    : overlap_width,
        'height'   : overlap_height,
    }