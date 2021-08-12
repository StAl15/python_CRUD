from db.articles import article_model

# print(article_model.create("Title2", "Content: Hello world! i don't know who am i", 8, 3423542543))
print(article_model.read_one(1))
print(article_model.read_many(2))
print(article_model.read_all())
# print(article_model.update(1, "update_title", "update_content", 777, 1989394))
print(article_model.delete(1))
#print(article_model.delete_all())
