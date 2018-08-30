import pandas as pd
import random


def get_duplicates(_df):
    return _df.loc[_df.duplicated(subset='file_name', keep=False), ["cf_id", "file_name"]].groupby("file_name").apply(set)


def main():
    # cf_files = ["test_file_" + str(i) for i in range(50)]
    # data = []
    # for i in xrange(50):
    #     data.append([i, random.choice(cf_files)])

    data = [[1, 'test1'], [2, 'test2'], [3, 'test1'], [4, 'test3'], [5, 'test2'], [6, 'test4']]

    df = pd.DataFrame(data, columns=['cf_id', 'file_name'])
    dup_df = get_duplicates(df)
    print dup_df

    # print df[df.is_duplicate == True]
    # df.drop_duplicates(subset="file_name", inplace=True)
    # print df


if __name__ == '__main__':
    main()