
def alarm_clock(day, vacation):
  if not vacation:
    if day == 6 or day == 0:
      return '10:00'
    else: 
      return '7:00'
  else:
    if day == 6 or day == 0:
      return 'off'
    else: 
      return '10:00'