import pandas as pd

company_relations = pd.read_csv("./company_relations.csv")
land_ownership = pd.read_csv("./land_ownership.csv")

def GetLands(company_id):

    result = company_relations.merge(land_ownership, on=["company_id"], how='right')
    directly_df = result[result.company_id == company_id].filter(items=['company_id','land_id','parent'])
    parent_df = result[result.company_id == company_id].filter(items=['company_id','land_id','parent']).drop_duplicates(['parent'])[['parent']]
    rowcount = len(result[result.company_id == company_id].filter(items=['land_id','parent']).index)
    
    return rowcount, parent_df

company_id = 'S996664111413'

lands_directly, parent_df = GetLands(company_id)
print('company_id ' + company_id + ' owns directly ' + str(lands_directly) + ' land(s)')

lands_total_indirectly = 0

while parent_df.empty is False:
    for parent in parent_df['parent']:
        print(parent)
        lands_indirectly, parent_df = GetLands(parent)
        print('parent company_id ' + parent + ' owns directly ' + str(lands_indirectly) + ' land(s)')
        lands_total_indirectly = lands_total_indirectly + lands_indirectly

print('Land that company owns in total ' + str(lands_directly + lands_total_indirectly))

# I've took python pandas framework to create simple and effective program code
# If I had more time I used different framework/libraries to improve performance and added few tests.