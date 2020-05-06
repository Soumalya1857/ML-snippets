import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        0- Administrative, an integer
        1- Administrative_Duration, a floating point number
        2- Informational, an integer
        3- Informational_Duration, a floating point number
        4- ProductRelated, an integer
        5- ProductRelated_Duration, a floating point number
        6- BounceRates, a floating point number
        7- ExitRates, a floating point number
        8- PageValues, a floating point number
        9- SpecialDay, a floating point number
        10- Month, an index from 0 (January) to 11 (December)
        11- OperatingSystems, an integer
        12- Browser, an integer
        13- Region, an integer
        14- TrafficType, an integer
        15- VisitorType, an integer 0 (not returning) or 1 (returning)
        16- Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    #raise NotImplementedError
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        evidence = []
        labels = []
        for row in reader:
            #evidence.append([cell for cell in row[:17]])
            temp = []
            for i in range(17):
                if i in (15,16,10):
                    if i == 16:
                        temp.append(1 if row[i]=="TRUE" else 0)
                    if i == 15:
                        #print(row[15])
                        temp.append(1 if row[i] == 'Returning_Visitor' else 0)
                    if i == 10:
                        if row[i] == 'Jan':
                            temp.append(0)
                        if row[i] == 'Feb':
                            temp.append(1)
                        if row[i] == 'March':
                            temp.append(2)
                        if row[i] == 'April':
                            temp.append(3)
                        if row[i] == 'May':
                            temp.append(4)
                        if row[i] == 'June':
                            temp.append(5)
                        if row[i] == 'July':
                            temp.append(6)
                        if row[i] == 'Aug':
                            temp.append(7)
                        if row[i] == 'Sept':
                            temp.append(8)
                        if row[i] == 'Oct':
                            temp.append(9)
                        if row[i] == 'Nov':
                            temp.append(10)
                        if row[i] == 'Dec':
                            temp.append(11)
                    
                else:
                    temp.append(row[i])
            
            evidence.append(temp)
            #labels.append(0 if row[17] == 'TRUE' else 1)
            if row[17] == "FALSE":
                labels.append(0)
            else:
                labels.append(1)
    #print(type(evidence))
    #print(labels)
    # print(evidence[0])
    # print(len(evidence[0]))
    # print(labels[0])
    return evidence,labels



def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    #raise NotImplementedError
    model = KNeighborsClassifier(n_neighbors = 1)
    model.fit(evidence,labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    #raise NotImplementedError
    length = len(labels)
    true1 = 0
    true2 = 0
    false1 = 0
    false2 = 0

    for i in range(length):
        if  labels[i] == True:
            true2 += 1
            if predictions[i] == True:
                true1 += 1

    for i in range(length):
        if  labels[i] == True:
            false2 += 1
            if predictions[i] == True:
                false1 += 1

    sensitivity = (true1//true2)
    specificity = (false1//false2)

    return sensitivity,specificity



if __name__ == "__main__":
    main()
