import sys
import re
train_file = 'hi_hdtb-ud-train.conllu'
test_file = 'hi_hdtb-ud-test.conllu'

lemma_count = {}

lemma_max = {}

training_stats = ['Wordform types' , 'Wordform tokens' , 'Unambiguous types' , 'Unambiguous tokens' , 'Ambiguous types' , 'Ambiguous tokens' , 'Ambiguous most common tokens' , 'Identity tokens']
training_counts = dict.fromkeys(training_stats , 0)

test_outcomes = ['Total test items' , 'Found in lookup table' , 'Lookup match' , 'Lookup mismatch' , 'Not found in lookup table' , 'Identity match' , 'Identity mismatch']
test_counts = dict.fromkeys(test_outcomes , 0)

accuracies = {}



train_data = open (train_file , 'r',encoding="utf8")


for line in train_data:
    
    
    if re.search ('\t' , line):

        field = line.strip().split('\t')

        form = field[1]
        lemma = field[2]

      
        if form in lemma_count:
            a = lemma_count[form]
            if lemma in a:
                a[lemma] += 1
            else:
                a[lemma] = 1
        else:
            lemma_count[form] = {}
            lemma_count[form][lemma] = 1
            
            





        
for form in lemma_count.keys():
   

training_counts['Wordform types'] = len(lemma_count)
count = 0
for form in lemma_count.keys():
    temp = lemma_count[form]
    for i in temp:
        count += temp[i]
training_counts['Wordform tokens'] = count

count1 = 0
for form in lemma_count.keys():
    temp1 = lemma_count[form]
    if len(temp1) ==1:
        count1 += 1
training_counts['Unambiguous types'] = count1
count2 = 0

for form in lemma_count.keys():
    temp2 = lemma_count[form]
    if len(temp2) ==1:
        for i in temp2:
            count2 = count2+ temp2[i]
training_counts['Unambiguous tokens'] = count2
training_counts['Ambiguous types'] = training_counts['Wordform types']- training_counts['Unambiguous types']  
training_counts['Ambiguous tokens'] = training_counts['Wordform tokens'] -training_counts['Unambiguous tokens']
count3 = 0
for form in lemma_count.keys():
    if form in lemma_count[form]:
        count3 += lemma_count[form][form]
training_counts['Identity tokens'] = count3
count4 = 0
for form in lemma_max.keys():
    if len(lemma_count[form]) >1:
        b = lemma_max[form]
        a = lemma_count[form][b]
        count4 += a
training_counts['Ambiguous most common tokens'] = count4
accuracies['Expected lookup'] = (training_counts['Unambiguous tokens'] + training_counts['Ambiguous most common tokens'])/training_counts['Wordform tokens']
accuracies['Expected identity'] = training_counts['Identity tokens']/training_counts['Wordform tokens']

test_data = open ('hi_hdtb-ud-test.conllu' , 'r',encoding="utf8")
Total =0
count_match = 0
count_found = 0
count_mismatch = 0
count_not_found = 0
count_Identity = 0
count_not_Identity =0
for line in test_data:

    if re.search ('\t' , line):
        Total = Total+1
        # Tokens represented as tab-separated fields
        field = line.strip().split('\t')

        # Word form in second field, lemma in third field
        form = field[1]
        lemma = field[2]
        if form in lemma_max:
            count_found += 1
            if lemma == lemma_max[form]:
                count_match += 1   
            else:
                count_mismatch += 1
                
            
                
                
                
                 
                
        else:
            count_not_found +=1
            if form == lemma:
                    count_Identity += 1
            else:
                count_not_Identity +=1
        
        
        
        
print(Total,count_found,count_match,count_mismatch,count_not_found,count_Identity,count_not_Identity)
test_counts['Total test items'] = Total
test_counts['Found in lookup table'] = count_found
test_counts['Lookup match'] = count_match
test_counts['Lookup mismatch'] = count_mismatch
test_counts['Not found in lookup table'] = count_not_found
test_counts['Identity match'] = count_Identity
test_counts['Identity mismatch']= count_not_Identity

accuracies['Lookup'] =  test_counts['Lookup match']/test_counts['Found in lookup table']

accuracies['Identity'] = test_counts['Identity match']/test_counts['Not found in lookup table']

accuracies['Overall'] = (test_counts['Lookup match']+test_counts['Identity match'])/test_counts['Total test items']


output = open ('lookup-output.txt' , 'w')

output.write ('Training statistics\n')

for stat in training_stats:
    output.write(stat + ': ' + str(training_counts[stat]) + '\n')

for model in ['Expected lookup' , 'Expected identity']:
    output.write(model + ' accuracy: ' + str(accuracies[model]) + '\n')

output.write('Test results\n')

for outcome in test_outcomes:
    output.write(outcome + ': ' + str(test_counts[outcome]) + '\n')

for model in ['Lookup' , 'Identity' , 'Overall']:
    output.write(model + ' accuracy: ' + str(accuracies[model]) + '\n')

output.close







