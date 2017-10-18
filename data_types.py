
#function that classifies different data types 
def main():

test1=45
test2="October"
test3=16.74


data_classifier(test1)

def data_classifier(test1):
    if isinstance(test1,int):
        print('int')
    if isinstance(test1,str):
        print('str')
    if isinstance(test1,float):
        print('float')
    if isinstance(test1,bool):
        print('bool')
    else:
        print('') 

if __name__ == '__main__':
    main()
















