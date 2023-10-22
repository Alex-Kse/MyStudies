pages = 100
lines = 50
simbols = 25
one_simbol = 4


byte_one_book = pages * lines * simbols * one_simbol
Mb_one_book = byte_one_book / (1024 * 1024) #Перевод из байта в Мб
books_on_disk = int(1.44 // Mb_one_book, )

print("Количество книг, помещающихся на дискету:", books_on_disk)
