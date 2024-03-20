sold_books = 120
sold_books_price = 450
sold_laptops = 40
sold_laptops_price = 45000
sold_pens = 1000
sold_pens_price = 40

month_income_books = sold_books * sold_books_price
month_income_laptops = sold_laptops * sold_laptops_price
month_income_pens = sold_pens * sold_pens_price

month_income = month_income_books + month_income_laptops + month_income_pens

average_price = month_income // (sold_books + sold_laptops + sold_pens)

print(f'Общий доход - {month_income}. Общий доход: за книги - {month_income_books}, за ноутбуки - {month_income_laptops}, за ручки - {month_income_pens}. Средняя цена всех товаров - {average_price} ')