
from datetime import datetime

dataTeste = "6/17/202010:02:03PM"
data = datetime.strptime(dataTeste, '%m/%d/%Y%H:%M:%S%p')
print(data)
