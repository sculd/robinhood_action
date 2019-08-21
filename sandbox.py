import auth

token = auth.get_token()
print(token)

import quote
print(quote.get_quotes(token, ['ASM']))
print(quote.get_ask_price(token, 'ASM'))


import account
print(account.get_account_url(token))


import instrument
print(instrument.get_instrument_url(token, 'ASM'))


import order
#print(order.order_status(token, '15390ade-face-caca-0987-9fdac5824701'))
order.buy_and_sell(token, 'ASM', 1, 0.01)
