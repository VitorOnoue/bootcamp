from datetime import datetime

time_now = datetime.now()
time_str = "02/07/2024-21.24"
mask_ptbr = "%Hh%M %d/%m/%Y %a"

print(time_now.strftime(mask_ptbr)) # converting a datetime to the format we want (in this case, brazilian date format)
print(datetime.strptime(time_str, "%d/%m/%Y-%H.%M")) # converting an awkward format (dd/mm/yy-hh.MM) to datetime