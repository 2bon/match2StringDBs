from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
def get2txt_similarity(t1,t2):
    try:
        cred = credential.Credential("AKIDvc4HK8Z088tOdeS0OchbKo45rNk3uvUp", "GMErPindFrTt4vXtzrVv50mJacPyHK7o")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.SentenceSimilarityRequest()
        params = '{"SrcText":"'+t1+'","TargetText":"'+t2+'"}'
        #params = '{"SrcText":"A相保护测量电压1","TargetText":"A相保护测量电压1s"}'
        req.from_json_string(params)

        resp = client.SentenceSimilarity(req)
        Similarity = resp.Similarity
        print(Similarity)
        return Similarity

    except TencentCloudSDKException as err:
        print(err)
