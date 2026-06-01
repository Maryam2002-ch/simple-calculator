print("\nDistinction it's a triangle or not.")

def get_angle(count):
    angle = input(f"{count} angle: ")
    return angle

def check_angle(angle):
    if not angle:
        print("\nplease fill the blank.")
        return None
    try:
        angle = int(angle)
        if angle == 0:
            print("\nPlease enter number greater than 0.")
            return None
    except ValueError:
            print("\nPlease enter valid size of angle.")
            return None
    
    return angle

def triangle():
    while True:
            f_angle = get_angle('First')
            
            f_angle = check_angle(f_angle)
            if not f_angle:
                continue
            else:
                break

    while True:
            s_angle = get_angle('Second')
                
            s_angle = check_angle(s_angle)
            if not s_angle:
                continue
            else:
                break
                
    while True:
            t_angle = get_angle('Third')
                
            t_angle = check_angle(t_angle)
            if not t_angle:
                continue
            else:
                break

    answer = f_angle + s_angle + t_angle
        
    if answer == 180:
        print("\nThis is a triangle.")
    else:
        print("\nThis is not triangle.")

    while True:
        yes_no = input("\nDo you want to continu? (yes/no)  ").strip().lower()
            
        if yes_no == 'yes':
            break
        elif yes_no == 'no':
            print("\nHave a good day.")
            return yes_no
        else:
            print("\nPlease enter valid answer.")
            continue

if __name__ == '__main__':
    triangle()




