# E-commerce
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# but writing all that on the 3 rd line is verbose to make it short we do what is below
from ecommerce.shipping import calc_shipping
calc_shipping()

# To only import the module in the package we do
from ecommerce import shipping
# And to use it 
shipping.calc_shipping()