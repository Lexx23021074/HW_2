'''Завдання 2

Створіть клас, який описує відгук до книги. 
Додайте до класу книги поле – список відгуків. 
Зробіть так, щоб при виведенні книги на екран за 
допомогою функції print також виводилися відгуки до неї.'''
class Review:
    def __init__(self, reviewer, text):
        self.reviewer = reviewer
        self.text = text
    
    def __str__(self):
        return f"Review by {self.reviewer}: {self.text}"