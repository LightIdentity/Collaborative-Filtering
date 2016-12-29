from similar import *

#
# Recommend books based on books your friends have rated
#

# Example dictionary of book ratings by person
ratings = { 'Joe': {'Brave New World': 4.5, 'Foundation': 5.0, 'Atlas Shrugged': 3.0, 'Oryx and Crake': 3.5 },
            'Tom': {'Brave New World': 2.0, 'Slaughterhouse Five': 5.0, 'Hunger Games': 2.0, 'Catcher in the Rye': 3.0},
            'Lisa': {'Slaughterhouse Five': 4.0, 'Catch-22': 3.0, 'Catcher in the Rye': 1.0},
            'Tim': {'Brave New World': 5.0, 'Oryx and Crake': 4.0, 'Slaughterhouse Five': 4.0, 'Catch-22': 3.0,
                    'Foundation': 3.0},
            'Chris': {'Catcher in the Rye': 3.5, 'Hunger Games': 3.5},
            'Michael': {'Catcher in the Rye': 1.5, 'Hunger Games': 5.0},
            'Laura': {'Slaughterhouse Five': 3.0, 'Catcher in the Rye': 2.0, 'Hunger Games': 1.5}
}

# Recommend books using user-based filtering
def recommend(person, similar_friends, ratings):
    total_cumsum = {}
    similarity_cumsum = {}

    # Iterate through each of your friends and find books you haven't read
    for friend in similar_friends:
        book_ratings = ratings[friend]

        for book in book_ratings:
            if book not in ratings[person]:

                # For each book, calculate a cumulative weighted total of ratings as well as cumulative similarity
                total_cumsum.setdefault(book,0)
                total_cumsum[book] += ratings[friend][book] * similar_friends[friend]

                similarity_cumsum.setdefault(book,0)
                similarity_cumsum[book] += similar_friends[friend]

    # Compute predicted recommended score and sort
    recommendations = [(total/similarity_cumsum[book], book) if similarity_cumsum[book]!=0 else (0, book)
                       for book,total in total_cumsum.items()]
    recommendations.sort()
    recommendations.reverse()

    return recommendations

# Recommend books using item-based filtering
def recommend_items(name, similar_items, ratings):
    total_cumsum = {}
    similarity_cumsum = {}

    for book in similar_items:
        for comp_book in similar_items[book]:

            total_cumsum.setdefault(comp_book[1],0)
            total_cumsum[comp_book[1]] += ratings[name][book] * comp_book[0]

            similarity_cumsum.setdefault(comp_book[1],0)
            similarity_cumsum[comp_book[1]] += comp_book[0]

    recommendations = [ (total/similarity_cumsum[book], book) if similarity_cumsum[book]!=0 else (0, book)
                        for book,total in total_cumsum.items()]
    recommendations.sort()
    recommendations.reverse()

    return recommendations

if __name__ == '__main__':
    your_name = 'Tim'

    similar_friends = most_similar('Tim', ratings)
    #print recommend(your_name, similar_friends, ratings)
    print

    new_ratings = transform(ratings)
    similar_items, books_read, books_not_read = most_similar_items(your_name, new_ratings)
    print recommend_items(your_name, similar_items, ratings)



