import pandas as pd
import numpy as np

class BreedsDataFeatureProcessor():
    """
    A class used to transform data from the Dogtime dataset. Formats data into
    one hot encoded style feature matrices and vector. Ultimately for usage with
    numpy's linear algebra math functions.

    Attributes
    ----------
    breeds__data : DataFrame
        data frame of breeds rating data from dogtime
    user_survey_data : DataFrame
        data frame of user data from our web service's survey
    adopted_data : DataFrame
        data frame of adopted data from animal protect system (or each center's)
    abandoned_data : DataFrame
        data frame of abandoned dogs data from animal protect system
    target_user : str
        string of user's unique id that we're trying to provide recommendations for

    Methods
    -------
    transform_adopted_dogs()
        Finds all dogs which has been adopted before. This returns 2 things as a tuple:
        1) Transforms adopted dogs categories into a one hot encoded feature matrix
        where columns correspond to categories and rows are different dogs
        2) Transforms those same adopted dogs into vector of breed ratings

    transform_entire_breeds_features() : breeds features + abandoned features
        Goes through entire DataFrame of self.breeds_data and transforms all dogs into
        a feature matrix. Will be used to score recommendations based on user weights
        for the top recommendations.

    """

    def __init__(self, target_user_id: str, target_user_dict, breeds_data, user_survey_data, adopted_data, abandoned_data):
        self.breeds_data = breeds_data
        self.user_survey_data = user_survey_data
        self.adopted_data = adopted_data
        self.abandoned_data = abandoned_data

        self.target_user_id = target_user_id

    def transform_adopted_dogs(self):
        pass

    def get_features(self, data):
        """
        :param data:
        :return: data columns
        """
        return data.columns

    def transform_entire_breeds_features(self):
        breeds_data_features = self.get_features(self.breeds_data)
        # user_survey_data_features = self.get_features(self.user_survey_data)
        # adopted_data_features = self.get_features(self.adopted_data)
        # abandoned_data_features = self.get_features(self.abandoned_data)

        # merge or join
        recommendation_features=breeds_data_features

        # final features for recommendation
        return recommendation_features
