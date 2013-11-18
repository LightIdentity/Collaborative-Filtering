import math

#
# Finds your most similar friends
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

# Compute correlation between 2 sets
def similar(your_set, other_set):
    n = 0
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    # Compute required values for Pearson Correlation
    for item in other_set:
        if item in your_set:
            n += 1
            sum_y += other_set[item]
            sum_y2 += pow(other_set[item],2)
            sum_xy += other_set[item]*your_set[item]

    for item in your_set:
        if item in other_set:
            sum_x += your_set[item]
            sum_x2 += pow(your_set[item],2)

    sum_x22 = pow(sum_x,2)
    sum_y22 = pow(sum_y,2)

    numerator = (n*sum_xy - (sum_x*sum_y))

    denominator = ((n*sum_x2-(sum_x22))*(n*sum_y2-(sum_y22)))**0.5

    # Ensure that denominator isn't 0
    if denominator == 0:
        return 0

    correlation = numerator/denominator

    return correlation

# Find most similar friends and return sorted decreasing
def most_similar(name, people):
    similar_friends = {}

    # Iterate through each person, check it doesn't match with your name, and find the correlation between the pair
    # of individuals
    for p in people:
        if p != name:
            # for book in people[p]:
            #     if people[p][book] in people[name]:
            #         friend_mutual_books[book] = people[p][book]
            #         your_mutual_books[book] = people[name][book]

            correlation = similar(people[name], people[p])
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

# Return list of similarities between each book you read and have haven't read
def most_similar_items(name, ratings):
    books_you_read = {}
    books_not_read = {}
    result = {}

    # Sort books based on which you read and didn't
    for item in ratings:
        if name in ratings[item]:
            books_you_read[item] = ratings[item]
        else:
            books_not_read[item] = ratings[item]

    print books_you_read
    print
    print books_not_read
    print

    # Computes similarity between books for item-based filtering
    similarity_list = []

    # Computer the correlation between each pair of books
    for book in books_you_read:
        for nbook in books_not_read:
            print book + ' ' + nbook
            print books_you_read[book]
            print books_not_read[nbook]
            print similar(books_you_read[book], books_not_read[nbook])
            print
            similarity_list.append((similar(books_you_read[book], books_not_read[nbook]), nbook))
        result[book] = similarity_list
        similarity_list = []

    return result

if __name__ == '__main__':
    your_name = 'Tim'
    print most_similar(your_name, ratings)
    print
    ratings = transform(ratings)
    print ratings
    print
    print most_similar_items(your_name, ratings)


