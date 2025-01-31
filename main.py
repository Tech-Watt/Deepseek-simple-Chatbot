data : list[int] = [3,4,5,8,5,6,3]

def stat(data:list) -> float:
    if not data:
        return None
    data_length = len(data)
    
    mean = sum(data) / data_length
    print(f'Mean is : {mean}')

    sorted_data = sorted(data)

    if data_length % 2 == 0:
        median = (sorted_data[data_length//2] + sorted_data[data_length//2-1])/2
        print(f'Median is {median}')

    else:
        median = sorted_data[data_length//2]
        print(f'Median is {median}')

    frequency = {}
    for i in sorted_data:
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i] = 1
    maxdict_value = max(frequency.values())

    mode = [key for key,value in frequency.items() if maxdict_value == value]
    print(f'Mode is : {mode}')

    result = []
    for key,value in frequency.items():
        if maxdict_value == value:
            result.append(key)
    print(result)
if __name__ == '__main__':
    stat(data)

"""
Given an array,X , of N integers and an array,W representing 
the respective weights of X's elements, calculate and print the
weighted mean of X's elements. Your answer should be rounded to 
a scale of  decimal place (i.e.,10.3  format).

Example:
X = [1,2,3]
W = [5,6,7]
The array of values .X[i] * W[i] = [5,12,21]
Their sum is 38. The sum of W 18. The weighted mean is 38/18 =2.1111.
Print 2.1 and return
"""


def weightedMean(X, W):
    # Write your code here
    weighted_list = []
    data_zipped = zip(X,W)
    for xi,wi in data_zipped:
        weighted_list.append(xi*wi)
    weighted_mean = sum(weighted_list)/sum(W)
    print(f'{weighted_mean:.1f}')
    