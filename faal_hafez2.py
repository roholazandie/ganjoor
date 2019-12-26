from ganjoor import Ganjoor
import random

ganj = Ganjoor()
poet_name = '\'حافظ\''
poems = ganj.get_poems(poet_name)
faal_id = random.randint(0, len(poems))
faal = [verse.text for verse in poems[faal_id].verses]
faal = '\n'.join(faal)
print(faal)