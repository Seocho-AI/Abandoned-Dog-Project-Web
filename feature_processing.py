import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer
import gc

panel = [
    'a_adaptability',
    'a1_adapts_well_to_apartment_living',
    'a2_good_for_novice_owners',
    'a3_sensitivity_level',
    'a4_tolerates_being_alone',
    'a5_tolerates_cold_weather',
    'a6_tolerates_hot_weather',
    'b_all_around_friendliness',
    'b1_affectionate_with_family',
    'b2_incredibly_kid_friendly_dogs',
    'b3_dog_friendly',
    'b4_friendly_toward_strangers',
    'c_health_grooming',
    'c1_amount_of_shedding',
    'c2_drooling_potential',
    'c3_easy_to_groom',
    'c4_general_health',
    'c5_potential_for_weight_gain',
    'c6_size',
    'd_trainability',
    'd1_easy_to_train',
    'd2_intelligence',
    'd3_potential_for_mouthiness',
    'd4_prey_drive',
    'd5_tendency_to_bark_or_howl',
    'd6_wanderlust_potential',
    'e_exercise_needs',
    'e1_energy_level',
    'e2_intensity',
    'e3_exercise_needs',
    'e4_potential_for_playfulness'
]

class BreedsDataFeatureProcessor():
    """
    A class used to transform data from the Dogtime dataset. Formats data into
    one hot encoded style feature matrices and vector. Ultimately for usage with
    numpy's linear algebra math functions.

    Attributes
    ----------
    breeds_panel : DataFrame
        data frame of breeds rating data from dogtime
    user_survey_data : DataFrame
        data frame of user data from our web service's survey
    adopter_data : DataFrame
        data frame of adopted data from animal protect system (or each center's)
    dog_list_data : DataFrame
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

    def __init__(self, target_user_id: str, breeds_panel, user_survey_data, adopter_data, dog_list_data, breed_info):
        self.target_user_id = target_user_id

        self.breeds_panel = breeds_panel
        self.user_survey_data = user_survey_data
        self.adopter_data = adopter_data
        self.dog_list_data = dog_list_data
        self.breed_info = breed_info
        self.target_user_id = target_user_id
        # 추천을 위해 필요한 columns:
        # dog_list_data
        #     유기 번호: PK
        #     나이: 자견, 성견 (원본 데이터 나이에 따라 수치로 변환 해야함)
        #     성별: 수컷, 암컷, 상관 없음 (원본 데이터 성별에 따라 수치로 변환 해야함)
        #     중성화 여부: 중성화 된 개체 원하면 3, 상관 없으면 2, 싫으면 1
        #     보호장소: 위치기반 구현할거면 추가
        #     믹스견분류결과: 믹스견 품종 하나로 그냥 고정하려고 필요
        #
        # breeds_panel
        #     해당 품종 panel, default=3
        #
        # adopter_data
        #     age_range, Not Null
        #     house_type, default=0 (null)
        self.processed_user_data = {
            'user_id': 111111, # user id or survey number
            'age': 3,
            'sexCd': 3, # m=1, f=2, don't care=3
            'neuterYn': 3, # yes=1, no=0
            'age_range': 3,
            'house_type': 3,
            'a_adaptability': 3,
            'a1_adapts_well_to_apartment_living': 3,
            'a2_good_for_novice_owners': 2,
            'a3_sensitivity_level': 1,
            'a4_tolerates_being_alone': 3,
            'a5_tolerates_cold_weather': 4,
            'a6_tolerates_hot_weather': 1,
            'b_all_around_friendliness': 1,
            'b1_affectionate_with_family': 2,
            'b2_incredibly_kid_friendly_dogs': 3,
            'b3_dog_friendly': 5,
            'b4_friendly_toward_strangers': 3,
            'c_health_grooming': 4,
            'c1_amount_of_shedding': 3,
            'c2_drooling_potential': 1,
            'c3_easy_to_groom': 1,
            'c4_general_health': 2,
            'c5_potential_for_weight_gain': 1,
            'c6_size': 4,
            'd_trainability': 3,
            'd1_easy_to_train': 4,
            'd2_intelligence': 5,
            'd3_potential_for_mouthiness': 3,
            'd4_prey_drive': 3,
            'd5_tendency_to_bark_or_howl': 3,
            'd6_wanderlust_potential': 5,
            'e_exercise_needs': 1,
            'e1_energy_level': 2,
            'e2_intensity': 2,
            'e3_exercise_needs': 4,
            'e4_potential_for_playfulness': 5
        }
        # user_age
        # user_house_type
        # user_dog_experience
        # neighbor_agreement
        # user_family_size
        # user_kids
        # dog_size
        # shedding_level
        # bark_tolerance
        # spend_time
        # spend_type
        # dog_sex
        # dog_environment
        # dog_support_agreement
        # dog_health_agreement
        self.user_age_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.user_house_type_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.user_dog_experience_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        # self.neighbor_agreement_dict = {
        #     '1': 1,
        #     '2': 2,
        #     '3': 3,
        #     '4': 4,
        #     '5': 5
        # }
        self.user_family_size_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.user_kids_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.dog_size_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.shedding_level_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.bark_tolerance_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.spend_time_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.spend_type_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.dog_sex_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.dog_environment_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.dog_health_agreement_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.want_dog_age_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5
        }
        self.neuter_yn = {
            '1': 1,
            '2': 2,
            '3': 3,
        }

    def mix_predict_processing(self):
        """
        예측 값 다 데이터베이스에 들어가면 주피터에서 업데이트 시켜서 db 수정
        :return:
        """
        pass

    # def get_features(self, data):
    #     """
    #     :param data:
    #     :return: data columns
    #     """
    #     return data.columns
    def processing_breeds_panel_features(self):
        # processing breeds_panel features
        breeds_panel = self.breeds_panel.drop(columns=['url', 'breed_group', 'height', 'weight', 'life_span'], errors='ignore')

        # breeds_panel.pop('url',None)
        # breeds_panel.pop('breed_group',None)
        # breeds_panel.pop('height',None)
        # breeds_panel.pop('weight',None)
        # breeds_panel.pop('life_span',None)
        gc.collect()
        # print("processing_breeds_panel_features Clear")
        return breeds_panel

    def processing_specialMark_features(self):
        """
        특징 데이터 자연어 처리 결과 수치로 변환해서 해당하는 panel data에 +-
        :return
        """
        pass

    def processing_user_survey_data_features(self):
        """
        # 추천을 위해 필요한 columns:
        dog_list_data
            유기 번호: PK
            나이: 자견, 성견 (원본 데이터 나이에 따라 수치로 변환 해야함)
            성별: 수컷, 암컷, 상관 없음 (원본 데이터 성별에 따라 수치로 변환 해야함)
            중성화 여부: 중성화 된 개체 원하면 3, 상관 없으면 2, 싫으면 1
            보호장소: 위치기반 구현할거면 추가
            믹스견분류결과: 믹스견 품종 하나로 그냥 고정하려고 필요

        breeds_panel
            해당 품종 panel, default=3

        adopter_data
            age_range, Not Null
            house_type, default=0 (null)

        :return: vectorized user_survey_data
        """
        # user_age: 나이대 가중치
        # user_house_type: 다가구주택,아파트 or 단독주택 a1
        # user_dog_experience: novice a2, b3
        # neighbor_agreement: 추천에 제외
        # user_family_size: b1, b4
        # user_kids: b1, b2, b4
        # dog_size: c6
        # shedding_level: c1
        # bark_tolerance: d5
        # spend_time: a4, e3
        # spend_type: e1, e4
        # dog_sex: column 추가해서 수치 넣기
        # dog_environment: x
        # dog_support_agreement: x
        # dog_health_agreement: x
        # age
        #print("dddd",user_survey_data2)
        user_survey_data = self.user_survey_data.copy()
        #print(user_survey_data.columns)
        # print(user_survey_data)
        self.processed_user_data['user_id'] = user_survey_data['user_id']
        #print(self.processed_user_data)
        age_dict={'20대이하': 1,
                    '30대': 2,
                    '40대': 3,
                    '50대': 4,
                    '60대이상': 5,
                  }
        self.processed_user_data['age'] = age_dict[user_survey_data['user_age']]

        # print(self.dog_list_data.columns)

        # print(dog_list_data[self.dog_list_data.loc[:,'sexCd']=='M'])
        # sexCd
        # self.processed_user_data['sexCd'] = self.user_survey_data['sexCd'].map({
        #     '남성': 1,
        #     '여성': 2,
        #     np.nan: 0
        # }, na_action=None)
        # dog_list_data[self.dog_list_data.loc['sexCd'] == 'M', 'sexCd'] = 1
        # dog_list_data[self.dog_list_data.loc['sexCd'] != 'M', 'sexCd'] = 2

        # neuterYn
        # self.processed_user_data['neuterYn'] = self.user_survey_data['neuterYn'].map({
        #     'Y': 1,
        #     'N': 1,
        #     'U': 1,
        #     np.nan: int(0)
        # }, na_action=None)
        # self.dog_list_data[self.dog_list_data.loc[:, 'neuterYn']=='Y', 'neuterYn'] = 1
        # self.dog_list_data[self.dog_list_data.loc[:, 'neuterYn']!='Y', 'neuterYn'] = 2

        # age_range
        # self.processed_user_data['age_range'] = self.user_survey_data['user_age'].map({
        #     '20대이하': 1,
        #     '30대': 2,
        #     '40대': 3,
        #     '50대': 4,
        #     '60대이상': 5,
        #     np.nan: int(0)
        # }, na_action=None)

        house_dict={
            '단독주택': 1,
            '다가구주택': 2,
            '아파트': 2,
            '원룸': 1,
            '기타': 3,
            np.nan: int(0)
        }
        # house_type
        self.processed_user_data['house_type'] = house_dict[user_survey_data['user_house_type']]
        # 나이 년생 숫자로 전처리 해야함
        # if self.dog_list_data['age']>2022:

        # print("processed_user_data = ", self.processed_user_data)
        # print("processing_user_survey_data Clear")

        return self.processed_user_data
    def processing_user_age(self):
        scaler = Normalizer()
        adopter = self.adopter_data.iloc[:, 2:-1]
        adopter_scaled = scaler.fit_transform(adopter)
        self.adopter_scaled = pd.DataFrame(adopter_scaled, columns=adopter.columns)
        # print("processing_user_age Clear")
    def processing_adopter_data_features(self):
        # processing adopter data
        self.processing_user_age()
        self.adopter_scaled['나이대'] = self.adopter_data.loc[:, '나이대']
        self.adopter_scaled['주거형태'] = self.adopter_data.loc[:, '주거형태']
        # print("processing_adopter_data_features Clear")
        return self.adopter_scaled

    def processing_dog_list_data_features(self):
        # processing dog_list features
        dog_list_data = self.dog_list_data.loc[:, :]
        breeds_panel = self.processing_breeds_panel_features()
        #print(dog_list_data.shape)
        dog_list_data=dog_list_data.drop(columns=['processState', 'specialMark', 'mixPredict', 'filename',
                                                  'happenDt',
                                                  'happenPlace',
                                                  'colorCd',
                                                  'weight',
                                                  'noticeNo',
                                                  'noticeSdt',
                                                  'noticeEdt',
                                                  'popfile',
                                                  'careNm',
                                                  'careTel',
                                                  'careAddr',
                                                  'orgNm',
                                                  'officetel'], errors='ignore')
        #print(dog_list_data.columns)
        gc.collect()

        # age
        dog_list_data['age'] = dog_list_data['age'].map({
            '2022(년생)': 1,
            '2021(년생)': 2,
            '2020(년생)': 3,
            '2019(년생)': 4,
            '2018(년생)': 5,
            '2017(년생)': 6,
            '2016(년생)': 7,
            np.nan: int(0)
        }, na_action=None)
        # print(self.dog_list_data.columns)

        # print(dog_list_data[self.dog_list_data.loc[:,'sexCd']=='M'])
        # setCd
        dog_list_data['sexCd'] = dog_list_data['sexCd'].map({
            'M': 1,
            'F': 2,
            np.nan: 0
        }, na_action=None)
        # dog_list_data[self.dog_list_data.loc['sexCd'] == 'M', 'sexCd'] = 1
        # dog_list_data[self.dog_list_data.loc['sexCd'] != 'M', 'sexCd'] = 2

        # neuterYn
        dog_list_data['neuterYn'] = dog_list_data['neuterYn'].map({
            'Y': 1,
            'N': 1,
            'U': 1
        }, na_action=None)
        # self.dog_list_data[self.dog_list_data.loc[:, 'neuterYn']=='Y', 'neuterYn'] = 1
        # self.dog_list_data[self.dog_list_data.loc[:, 'neuterYn']!='Y', 'neuterYn'] = 2

        # age_range
        dog_list_data['age_range'] = self.adopter_scaled['나이대'].map({
            '20대이하': 1,
            '30대': 2,
            '40대': 3,
            '50대': 4,
            '60대이상': 5
        }, na_action=None)

        # house_type
        dog_list_data['house_type'] = self.adopter_scaled['주거형태'].map({
            '단독주택': 1,
            '다가구주택': 2,
            '아파트': 3,
            '원룸': 4,
            '기타': 5
        }, na_action=None)
        # 나이 년생 숫자로 전처리 해야함
        # if self.dog_list_data['age']>2022:
        cnt=0
        # 추후 수정
        # print(breeds_panel.columns)
        # print(self.breed_info.columns)
        # print(dog_list_data.columns)
        # print(breeds_panel.head())
        # print(self.breed_info.head())
        # print(self.dog_list_data.head())
        #print(self.breed_info[self.breed_info['breed_name_kr'].values == dog_list_data['kindCd'].values])
        # dog = dog_list_data.loc[dog_list_data['desertionNo'] == '411304202200536']
        # print(dog_list_data.loc[dog_list_data['desertionNo'] == '411304202200536'])

        # print(type(dog_list_data))
        # print(type(panel))
        for i in dog_list_data['desertionNo'].values:
            breed_kr = dog_list_data.loc[dog_list_data['desertionNo'] == i, 'kindCd'].values[0]
            # print(breed_kr)
            if breed_kr not in self.breed_info['breed_name_kr'].values:
                continue
            breed_en = self.breed_info.loc[self.breed_info['breed_name_kr'] == breed_kr, 'breed_name'].values[0]
            # print(breed_en)
            if breed_en not in self.breeds_panel['breed'].values:
                continue
            for key in panel:
                # print(key)

                panel_rating = self.breeds_panel.loc[self.breeds_panel['breed'] == breed_en, key]
                #print(panel_rating)
                dog_list_data.loc[dog_list_data['desertionNo'] == i, key] = panel_rating.values[0]
                #print(dog_list_data[dog_list_data['desertionNo']==i])
            # cnt+=1
            # print(cnt)
            # print("processing_dog_list_data_features Clear")
        # print(dog_list_data.columns)
        return dog_list_data

    def processing_all_features(self):
        # breeds_panel_features = self.get_features(self.breeds_panel)
        # user_survey_data_features = self.get_features(self.user_survey_data)
        # adopter_data_features = self.get_features(self.adopter_data)
        # dog_list_data_features = self.get_features(self.dog_list_data)
        # print("processing_all_features")
        return self.processing_breeds_panel_features(),\
               self.processing_user_survey_data_features(),\
               self.processing_adopter_data_features(),\
               self.processing_dog_list_data_features()

    def transform(self):
        processed_breeds_panel, processed_user_data, adopter_data, processed_dog_list = self.processing_all_features()
        # print("processing_all_features Clear")
        # print(processed_user_data)
        processed_dog_list=processed_dog_list.drop(columns=['kindCd'])
        gc.collect()
        return processed_user_data, processed_dog_list
