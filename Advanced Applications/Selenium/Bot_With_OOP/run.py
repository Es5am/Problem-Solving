from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.select_destination()
    bot.select_date('2026-03-05','2026-03-18')
    bot.select_adult(10)