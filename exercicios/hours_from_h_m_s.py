def hours_from_h_m_s(h, m, s):
    return h * 3600 + m * 60 + s


if __name__ == '__main__':
    h = int(input("Enter the hours: "))
    m = int(input("Enter the minutes: "))
    s = int(input("Enter the seconds: "))
    seconds = hours_from_h_m_s(h, m, s)
    
    print("The number of seconds is:", seconds)
