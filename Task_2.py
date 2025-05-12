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
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []  # список відгуків

    def add_review(self, review):
        self.reviews.append(review)

    def __str__(self):
        reviews_str = '\n'.join(str(review) for review in self.reviews)
        return f"Book: {self.title} by {self.author}\nReviews:\n{reviews_str if reviews_str else 'No reviews yet.'}"