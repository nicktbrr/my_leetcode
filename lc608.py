import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    temp = tree.merge(tree, left_on='id', right_on='p_id', how='left')
    temp = temp.drop_duplicates('id_x')
    def cat(row):
        if pd.isna(row['p_id_x']):
            return 'Root'
        elif pd.isna(row['id_y']):
            return 'Leaf'
        else:
            return 'Inner'
    temp['type'] = temp.apply(cat, axis=1)
    return pd.DataFrame({'id': temp['id_x'], 'type': temp['type']})


df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'p_id': [None, 1, 1, 2, 2]
})
print(tree_node(df))