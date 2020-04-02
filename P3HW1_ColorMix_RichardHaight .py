  # CTI-110
    # P3HW1 - Color Mixer
    # Your Name
    # Date
    #
#Choose Color one
primary_color1 = input (' Choose a primary color 1: ')

#Choose Color Two
primary_color2 = input (' Choose a primary color 2: ')

#red and blue makes purple
#red and yellow makes orange
#blue and yellow makes green

if ( primary_color1 == 'red' and primary_color2 == 'blue') or \
                 ( primary_color1 == 'blue' and primary_color2 == 'red'):
                 print( primary_color1 + ' mixed with ' + primary_color2 + ' is purple')
elif ( primary_color1 == 'red' and primary_color2 == 'yellow') or \
                 ( primary_color1 == 'yellow' and primary_color2 == 'red'):
                 print( primary_color1 + ' mixed with ' + primary_color2 + ' is purple')
elif ( primary_color1 == 'blue' and primary_color2 == 'yellow') or \
                 ( primary_color1 == 'yellow' and primary_color2 == 'yellow'):
                 print( primary_color1 + ' mixed with ' + primary_color2 + 'is purple')
else:
      print( ' Error ')


        
