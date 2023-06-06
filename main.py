from Zillow import Zillow
from Form import Form


zillow = Zillow()
zillow.get_zillow_data()
zillow.quit()

form = Form()
form.input_form_data(
    addresses = zillow.addresses_list, 
    prices = zillow.prices_list,
    links = zillow.links_list)

