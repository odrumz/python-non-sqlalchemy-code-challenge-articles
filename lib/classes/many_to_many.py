# class Article:
#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title
        
# class Author:
#     def __init__(self, name):
#         self.name = name

#     def articles(self):
#         pass

#     def magazines(self):
#         pass

#     def add_article(self, magazine, title):
#         pass

#     def topic_areas(self):
#         pass

# author1 = Author("James")

# class Magazine:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     def articles(self):
#         pass

#     def contributors(self):
#         pass

#     def article_titles(self):
#         pass

#     def contributing_authors(self):
#         pass

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        if not isinstance(author, Author):
           raise ValueError("Author must be of type Author.")
        if not isinstance(magazine, Magazine):
           raise ValueError("Magazine must be of type Magazine.")
        self.author = author
        self.magazine = magazine
        self.title = title  

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            print("Invalid title value. Title must be a string between 5 and 50 characters.")


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.name = name
        self.articles = set()
        self.magazines = set()

    def name(self):
        return self.name
    def articles(self):
        pass
        return self.articles

    def magazines(self):
        pass
        return self.magazines

    def add_article(self, magazine, title):
        pass
        if magazine not in self.magazines:
            raise ValueError('The specified magazine is not associated with this author.')
        article = Article(self, magazine, title)
        self.articles.append(article)
        magazine.add_article(article)

    def topic_areas(self):
        pass
        return set(article.topic_areas for article in self.articles)

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self.name = name

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.category = category

        self.articles = []
        self.contributors = []

    def articles(self):
        pass

    def contributors(self):
        pass
        return self.articles
    def add_article(self,article):
        if article.magazine != self:
            raise ValueError("The specified article is not associated with this magazine.")
        self.articles.append(article)
        article.magazine = self

    def article_titles(self):
        pass
        return [article.title for article in self.articles]

    def contributing_authors(self):
        pass
        return [author.name for author in self.contributors]
