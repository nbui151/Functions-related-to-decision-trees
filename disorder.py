def simple_disorder(category, outcome):
    # category is a list/vector of the features in a category 
    # outcome is a list/vector of the outcomes corresponding to category
    category = np.array(category)
    outcome = np.array(outcome)
    cat = list(set(category))
    out = list(set(outcome))
    
    # list to store the disorder in each category 
    all_disorder = []
    
    # iterate over each category 
    for m in cat:
        cat_num = 0
        outcome_by_cat = []
        for i in range(len(category)):
            if category[i] == m :
                # calculate the total number of obs in a category
                cat_num += 1 
                # put obs from the category in a list 
                outcome_by_cat.append(outcome[i])     
        # calculate the frequency of the values of obs in the category 
        outcome_dict = defaultdict(int)
        for i in outcome_by_cat:
            outcome_dict[i] += 1     
        # calculate disorder in each category 
        disorder = 0
        k = list(outcome_dict.values())
        for i in range(len(k)):
            disorder += -(k[i]/cat_num)*math.log(k[i]/cat_num,2)      
        # multiple by the obs in the category 
        cat_disorder = disorder * cat_num/len(outcome)     
        # append to list 
        all_disorder.append(cat_disorder)             
        # return sum of all the disorders of all categories 
    return sum(all_disorder)

def dataset_disorder(X, Y):  
    disorder_score = {}
    for i in X.columns: 
        category = X[i]
        disorder_score[i] = simple_disorder(category, Y)
    disorder_score_sort = sorted(disorder_score.items(), key=operator.itemgetter(1))
    disorder_value = disorder_score_sort[0][1]
    select_cat = disorder_score_sort[0][0]
    return select_cat, disorder_value


def one_layer(data, Y_column_name):
    Y = data[Y_column_name]
    X = data.drop(Y_column_name, axis = 1)
    results = dataset_disorder(X, Y)
    print("Should split by variable {}, disorder score is {}.".format(results[0], results[1]))
    return results 

def two_layers(data, Y_column_name):
    Y = data[Y_column_name]
    X = data.drop(Y_column_name, axis = 1)
    results = dataset_disorder(X, Y)
    print("Should split by variable {}, disorder score is {}.".format(results[0], results[1]))
    if results[1] == 0:
        print("End of tree")
        return results 
    if results[1] > 0: 
        select_cat = str(results[0])
        C = list(set(X[select_cat]))
        results_stop = {} 
        results_keep = {}
        for i in range(len(C)):
            key = C[i]
            data_sub = data.loc[data[select_cat] == C[i]]
            Y_sub = data_sub[Y_column_name]
            X_sub = data_sub.drop(Y_column_name, axis = 1)
            results = dataset_disorder(X_sub, Y_sub)
            if results[1] == 0: 
                results_stop[key] = results 
            if results[1] > 0: 
                results_keep[key] = results
        if len(results_stop) > 0: 
            print("These variables create pure splits:")
            print(results_stop)
        if len(results_keep) > 0: 
            print("These variables do not create pure splits:")
            print(results_keep)
        return results_stop, results_keep 
       
