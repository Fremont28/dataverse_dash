
#function that classifies different data types 
def main():

    test_data= "october"
    data_classifier(test_data)

def data_classifier(test_data):
    if isinstance(test_data,tuple): #(s,tuple)
        print('tuple') 
    if isinstance(test_data,str):
        print('str')
    if isinstance(test_data,float):
        print('float')
    if isinstance(test_data,bool):
        print('bool')
    else:
        print('') 

if __name__ == '__main__':
    main()
















