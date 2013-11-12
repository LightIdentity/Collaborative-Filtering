import math

#
# Finds your most similar friends
#

# Example dictionary of book ratings by person
ratings = { 'Joe': {'Brave New World': 4.5, 'Foundation': 5.0, 'Atlas Shrugged': 3.0, 'Oryx and Crake': 3.5 },
            'Tom': {'Brave New World': 2.0, 'Slaughterhouse Five': 5.0, 'Hunger Games': 2.0},
            'Lisa': {'Slaughterhouse Five': 4.0, 'Catch-22': 3.0, 'Catcher in the Rye': 1.0},
            'Tim': {'Brave New World': 5.0, 'Oryx and Crake': 4.0, 'Slaughterhouse Five': 4.0, 'Catch-22': 3.0,
                    'Foundation': 3.0}
}

# Compute similarity of interests between two individuals for user-based filtering
def similar(person, friend):
    friend_mutual_books = {}
    your_mutual_books = {}

    # Find mutual books
    for book in friend:
        if book in person:
            friend_mutual_books[book] = friend[book]
            your_mutual_books[book] = person[book]

    # Calculate Pearson Correlation Coefficient
    n = len(friend_mutual_books)
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0

    # Compute required values for Pearson Correlation
    for book in friend_mutual_books:
        sum_y += friend_mutual_books[book]
        sum_y2 += pow(friend_mutual_books[book],2)
        sum_xy += friend_mutual_books[book]*your_mutual_books[book]

    for ybook in your_mutual_books:
        sum_x += your_mutual_books[ybook]
        sum_x2 += pow(your_mutual_books[ybook],2)

    sum_x22 = pow(sum_x,2)
    sum_y22 = pow(sum_y,2)

    numerator = ((n*sum_xy) - (sum_x*sum_y))
    denominator = math.sqrt((n*sum_x2-sum_x22)*(n*sum_y2-sum_y22))

    # Ensure that denominator isn't 0
    if denominator == 0 :
        return 0

    correlation = numerator/denominator

    return correlation

# Find most similar friends and return sorted decreasing
def most_similar(person, people):
    similar_friends = {}

    for p in people:
        if p != person:
            correlation = similar(people[person], people[p])
            similar_friends[p] = correlation

    sorted(similar_friends.items(), key=lambda x:x[1])

    return similar_friends

# Inverts the ratings so you get the ratings of each individual for a particular book. Used for item-based filtering
def transform(ratings):
    transformed_ratings = {}
    for person in ratings:
        for r in ratings[person]:
            transformed_ratings.setdefault(r,{})
            transformed_ratings[r][person] = ratings[person][r]

    return transformed_ratings

# Computes similarity between items for item-based filtering
# Needs fixing  
def similar_items(ratings):
    result = {}

    for item in ratings:
        scores = similar(ratings[item], ratings)
        result[item] = scores

    return result

if __name__ == '__main__':
    your_name = 'Tim'
    print most_similar(your_name, ratings)
    print
    ratings = transform(ratings)
    print ratings
    print similar_items(ratings)
