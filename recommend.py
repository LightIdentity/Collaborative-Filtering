from similar import *

#
# Recommend books based on books your friends have rated
#

# Example dictionary of book ratings by person
ratings = { 'Joe': {'Brave New World': 4.5, 'Foundation': 5.0, 'Atlas Shrugged': 3.0, 'Oryx and Crake': 3.5 },
            'Tom': {'Brave New World': 2.0, 'Slaughterhouse Five': 5.0, 'Hunger Games': 2.0},
            'Lisa': {'Slaughterhouse Five': 4.0, 'Catch-22': 3.0, 'Catcher in the Rye': 1.0},
            'Tim': {'Brave New World': 5.0, 'Oryx and Crake': 4.0, 'Slaughterhouse Five': 4.0, 'Catch-22': 3.0,
                    'Foundation': 3.0}
}

# Recommend books not already read
def recommend(person, similar_friends, ratings):
    recommendations = []
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
    recommendations = [(total/similarity_cumsum[book], book) for book,total in total_cumsum.items()]
    recommendations.sort()
    recommendations.reverse()

    return recommendations

if __name__ == '__main__':
    your_name = 'Tim'
    similar_friends = most_similar('Tim', ratings)
    print similar_friends
    print recommend(your_name, similar_friends, ratings)


