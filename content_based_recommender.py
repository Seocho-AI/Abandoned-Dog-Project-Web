import pandas as pd
import numpy as np
from feature_processing import BreedsDataFeatureProcessor
from sklearn.metrics.pairwise import cosine_similarity

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

    def __init__(self, breeds_panel, user_survey_data, adopter_data, dog_list_data):
        self.breeds_panel = breeds_panel
        self.user_survey_data = user_survey_data
        self.adopter_data = adopter_data
        self.dog_list_data = dog_list_data

    def predict(self, target_user_dict, target_user_id: str = None):
        """
        fit takes in a target_user str and transforms all relevant, breeds data to train
        the model. Recommend breeds indices will be in self. recommendations.
        To look at specific scores refer to self._breed_rec_scores

        :param target_user_id: str user_id from user_survey_data

        """
        user_survey_data=pd.Series(target_user_dict)
        #print(self.user_survey_data)
        self.target_user_id = target_user_id
        self.target_user_dict = target_user_dict
        self._transform = BreedsDataFeatureProcessor(
            target_user_id=self.target_user_id,
            target_user_dict=self.target_user_dict,
            breeds_panel=self.breeds_panel,
            user_survey_data=user_survey_data,
            adopter_data=self.adopter_data,
            dog_list_data=self.dog_list_data
        )
        # print("BreedsDataFeatureProcessor Call Clear")
        # get breeds features and ratings

        processed_user_data, processed_dog_list = self._transform.transform()
        # print("transform Clear")
        processed_user_data = pd.DataFrame.from_dict(processed_user_data, orient='index')
        # print(processed_user_data)
        # print(processed_dog_list)
        #print(self.dog_list_data.shape)
        #processed_user_data.index = processed_user_data.index.astype(dtype='int64', copy=True)
        #print(self.user_survey_data.columns, self.breeds_data.columns)

        # print(processed_user_data)

        # print(processed_dog_list[processed_dog_list.isnull()==True])

        processed_dog_list = processed_dog_list.fillna(3) # null값 예외처리 해야함 8/27
        processed_dog_list['sexCd'] = processed_dog_list.loc[:, 'sexCd'].astype(dtype='int64')

        # print(len(self.dog_list_data))
        #print(processed_dog_list.isnull())
        #print(processed_user_data)
        #print(processed_dog_list)
        # self._breed_rec_scores = cosine_similarity(self.user_survey_data, self.breeds_data).argsort()[:, ::-1]
        self._breed_rec_scores = cosine_similarity(processed_user_data.T, processed_dog_list).argsort()[:, ::-1]
        # print("user_id=", processed_user_data['user_id'])
        #print(processed_dog_list.columns)
        self.recommendations = self.find_sim_breeds(user_survey_data=processed_user_data,
                                                    dog_list=self.dog_list_data,
                                                    sim_df=self._breed_rec_scores,
                                                    top_n=100) # 전체: len(self.dog_list_data)

        return list(self.recommendations['desertionNo'])


    def find_sim_breeds(self, user_survey_data, dog_list, sim_df, target_user_id=None, top_n=10):
        #user_survey_data.reset_index(inplace=True)
        # print(user_survey_data)
        #print(user_survey_data.columns)
        #user_id = user_survey_data[user_survey_data['userId'] == target_user_id]
        # print(sim_df)
        #print(user_id)

        user_index = user_survey_data.values
        #print("user_index=", user_index)
        similar_indexes = sim_df[:, :top_n]

        # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임.
        #dataframe에서 index로 사용하기 위해서 1차원 array로 변경
        #print(similar_indexes)
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

