import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # dict = {}
    # for i in range(len(person)):
    #     id = person['id'][i]
    #     email = person['email'][i]
    #     if email in dict:
    #         if dict[email] > id:
    #             dict[email] = id
    #     else:
    #             dict[email] = id
    # print(dict)
    # result = []
    # for key,value in dict.items():
    #     result.append([value,key])

    # df = pd.DataFrame(result,columns =['id', 'email'])
    # print(df)
    #sol2
    # person.sort_values(['id'], inplace = True)
    # person.drop_duplicates(['email'],inplace = True)

    #sol3
    min_id = person.groupby('email')['id'].transform('min')
    print(min_id)
    remove_id = person[person['id'] != min_id]
    print(remove_id)
    person.drop(remove_id.index, inplace = True)

      
           

    