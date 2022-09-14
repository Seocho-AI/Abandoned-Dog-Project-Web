import pandas as pd
import numpy as np
from model.feature_processing import BreedsDataFeatureProcessor
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import ndcg_score
from sqlalchemy import create_engine
import pymysql

class ContentBasedRecommender():
    """
    A class used to select a target user to provide recommendations.
    Model will transform data, fit the data (for the specified user), than predict the top
    recommendations for the user.

    Attributes
    ----------
    breeds__panel : DataFrame
        data frame of breeds rating data from dogtime
    user_survey_data : DataFrame
        data frame of user data from our web service's survey
    adopter_data : DataFrame
        data frame of adopted data from animal protect system (or each center's)
    dog_list_data : DataFrame
        data frame of abandoned dogs data from animal protect system
    target_user : str
        string of user's unique id that we're trying to provide recommendations for
    recommendations : ndarray
        numpy array of breeds indices to be recommended after using fit()
    _breed_rec_score : ndarray
        numpy array of Breeds where columns are Breed indices and
        carculated recommendation scores by cosine-similarity
    _breed_rec_valid : ndarray
        numpy array of Breeds where columns are Breed indices and
        carculated recommendation scores by Normalized Discounted Cumulative Gain (NDCG)
    _transform : BreedsDataFeatureProcessor
        class that contains the methods to transform dogtime dataset into feature
        matrices/feature vectors for model building/usage

    Methods
    -------
    fit(target_user)
        train the model using a specified target_user (id) from the user_data set.
        This function transforms all the necessary data and performs calculations
        using that trained info

    predict()
        return list of recommendations for the user sorted by top-rated breeds for th user


    """

    def __init__(self, target_user_survey, breeds_panel, adopter_data, dog_list_data, breed_info, panel_info,processed_dog_data_db=None):
        self.breeds_panel = breeds_panel
        self.panel_info = panel_info
        self.user_survey_data = target_user_survey
        self.adopter_data = adopter_data
        self.dog_list_data = dog_list_data
        self.breed_info = breed_info
        self.recommendations = []
        self.processed_dog_data_db = processed_dog_data_db
        user_survey_data=pd.Series(self.user_survey_data)
        self.target_user_id = None
        self._transform = BreedsDataFeatureProcessor(
            target_user_id=self.target_user_id,
            user_survey_data=user_survey_data,
            breeds_panel=self.breeds_panel,
            adopter_data=self.adopter_data,
            dog_list_data=self.dog_list_data,
            breed_info=self.breed_info,
            panel_info=self.panel_info,
            processed_dog_data_db=self.processed_dog_data_db
        )

    def fit(self, target_user_survey, breeds_panel, adopter_data, dog_list_data, breed_info):
        self.breeds_panel = breeds_panel
        self.user_survey_data = target_user_survey
        self.adopter_data = adopter_data
        self.dog_list_data = dog_list_data
        self.breed_info = breed_info

    def fit_transform(self, target_user_survey, target_user_id = None):
        """
        fit takes in a target_user str and transforms all relevant, breeds data to train
        the model. Recommend breeds indices will be in self. recommendations.
        To look at specific scores refer to self._breed_rec_scores

        :param target_user_id: str user_id from user_survey_data

        """


        #print(self.user_survey_data)


        user_survey_data=pd.Series(self.user_survey_data)
        self.target_user_id = target_user_id
        self._transform = BreedsDataFeatureProcessor(
            target_user_id=self.target_user_id,
            user_survey_data=user_survey_data,
            breeds_panel=self.breeds_panel,
            adopter_data=self.adopter_data,
            dog_list_data=self.dog_list_data,
            breed_info=self.breed_info,
            panel_info=self.panel_info,
            processed_dog_data_db=self.processed_dog_data_db

        )


        # print("BreedsDataFeatureProcessor Call Clear")
        # get breeds features and ratings
        # print(self.breeds_panel.columns)
        # print(self.breed_info.columns)
        processed_user_data, self.processed_dog_list = self._transform.transform()
        # print("transform Clear")
        processed_user_data = pd.DataFrame.from_dict(processed_user_data, orient='index')
        # print(processed_user_data)
        # print(processed_dog_list)
        #print(self.dog_list_data.shape)
        #processed_user_data.index = processed_user_data.index.astype(dtype='int64', copy=True)
        #print(self.user_survey_data.columns, self.breeds_data.columns)

        # print(processed_user_data)
        # print(processed_dog_list.isnull())

        # print(processed_dog_list[processed_dog_list.isnull()==True])
        # print(processed_dog_list)
        # processed_dog_list = processed_dog_list.fillna(3) # null값 예외처리 해야함 8/27
        processed_dog_list = self.processed_dog_list.dropna() # null값 예외처리 해야함 8/27
        #processed_dog_list['sexCd'] = processed_dog_list.loc[:, 'sexCd'].astype(dtype='int64')

        # print(len(self.dog_list_data))
        #print(processed_dog_list.isnull())
        # print(processed_user_data.columns)
        # print(processed_user_data.T)
        # # print(processed_dog_list.columns)
        # print(processed_dog_list.head())
        # db_connection_str = 'mysql+pymysql://kaist:0916@abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com/abandoned_dog'
        # db_connection = create_engine(db_connection_str)
        # conn = db_connection.connect()
        # processed_dog_list.to_sql(name="processed_dog_data", con=conn, if_exists='append',index=False)
        # print("to_db clear")



        # print(processed_user_data.head())
        # print(processed_dog_list.head())

        self.processed_user_data = processed_user_data
        self.processed_dog_list = processed_dog_list

    def predict(self, user_survey_data):
        # print("before", self.processed_dog_list)
        # self._breed_rec_scores = cosine_similarity(self.user_survey_data, self.breeds_data).argsort()[:, ::-1]
        #self.processed_user_data=self._transform.processing_user_survey_data_features(user_survey_data=user_survey_data)
        #processed_user_data = pd.DataFrame.from_dict(self.processed_user_data, orient='index')

        self.processed_user_data = self.processed_user_data.T.set_index('user_id')
        self.processed_dog_list = self.processed_dog_list.set_index('desertionNo')

        if len(self.processed_dog_list) == 0:
            print("해당 품종이 없습니다.")
            return [], []
        self._breed_rec_scores = cosine_similarity(self.processed_user_data, self.processed_dog_list)

        sorted_scores = sorted(self._breed_rec_scores[0], reverse=True)


        self._breed_rec_scores=self._breed_rec_scores.argsort()[:, ::-1]
        # print(self._breed_rec_scores)
        #print(processed_dog_list.columns)
        top_n = len(self.processed_dog_list)
        self.recommendations = self.find_sim_breeds(user_survey_data=self.processed_user_data,
                                                    dog_list=self.processed_dog_list,
                                                    sim_df=self._breed_rec_scores,
                                                    top_n=top_n) # 전체: len(self.dog_list_data)
        # print(self.recommendations)
        # print(self.NDCG(self.processed_user_data, self.recommendations['desertionNo']))

        return list(self.recommendations.index), sorted_scores[:top_n]

    def find_sim_breeds(self, user_survey_data, dog_list, sim_df, target_user_id=None, top_n=10):
        # user_survey_data.reset_index(inplace=True)
        # print(user_survey_data['user_id'])
        # print(type(user_survey_data))
        # user_id = user_survey_data['user_id']
        # print(sim_df)
        #print(user_id)
        # print("sim_df",sim_df)
        # print(dog_list)
        # user_index = user_survey_data['user_id']
        #print("user_index=", user_index)
        similar_indexes = sim_df[:, :top_n]

        # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임.
        #dataframe에서 index로 사용하기 위해서 1차원 array로 변경
        # print(similar_indexes)
        similar_indexes = similar_indexes.reshape(-1)
        return dog_list.iloc[similar_indexes]
    # def predict(self):
    #     """
    #     predict will return the breeds_data DataFrame sorted by highly recommended breeds
    #     at the top-n.
    #
    #     :return: DataFrame of breeds sorted by recommendation score descending
    #     """
    #
    #     return list(self.recommendations.index)
    # Normalized Discount Cumulative Gain
    # def NDCG(self, user, recBreeds):
        # print("NDCG: ")
        # print(user.columns)
        # print(self.processed_dog_list.columns)
        # print(recBreeds)
        # for idx in recBreeds:
        #     print(idx)
        #     print(ndcg_score(user, self.processed_dog_list[self.processed_dog_list.index == idx]))

    def get_processed_user_data(self):
        return self.processed_user_data.T.to_dict()

    def get_processed_dog_data(self):
        # print(self.processed_dog_list.index)
        # print(self.recommendations.index)
        # print(type(self.recommendations))
        # print(self.recommendations)
        if len(self.recommendations) == 0:
            return []

        processed_dog_data = self.processed_dog_list[self.processed_dog_list.index.isin(self.recommendations.index)]
        dicted_dog_list = processed_dog_data.T.to_dict()
        #print(dicted_dog_list)
        lst=[{key:val} for key, val in dicted_dog_list.items()]
        # for desertionNo in list(self.recommendations['desertionNo']):
        #     lst.append(self.processed_dog_list[self.processed_dog_list['desertionNo'] == desertionNo].to_dict())
        dic={}
        for key in lst:
            for k,v in key.items():
                dic[k]=v

        return dic
        # return lst

    def get_user_dog_diff(self):
        processed_dog_data = self.processed_dog_list[self.processed_dog_list.index.isin(self.recommendations.index)]
        processed_user_data = self.processed_user_data
        # print(processed_user_data)
        # print(processed_dog_data)
        processed_dog_data = processed_dog_data.loc[:,:].sub(processed_user_data.values, axis='columns').abs()

        dicted_dog_list = processed_dog_data.T.to_dict()
        lst=[{key:val} for key, val in dicted_dog_list.items()]
        dic={}
        for key in lst:
            for k,v in key.items():
                dic[k]=v
        return dic
